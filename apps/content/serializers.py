from rest_framework import serializers
from .models import MediaItem, Article, Section, Term


class MediaItemSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model  = MediaItem
        fields = ['id', 'title', 'media_type', 'description',
                'file_url', 'youtube_url', 'created_at']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file and request:
            return request.build_absolute_uri(obj.file.url)
        return None


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Section
        fields = ['id', 'section_type', 'title', 'content', 'order']


class TermSerializer(serializers.ModelSerializer):
    media_item = MediaItemSerializer(read_only=True)

    class Meta:
        model  = Term
        fields = ['id', 'slug', 'label', 'media_item']


class ArticleListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for article listings."""
    class Meta:
        model  = Article
        fields = ['id', 'title', 'subtitle', 'slug', 'created_at']


class ArticleDetailSerializer(serializers.ModelSerializer):
    """
    Full article with rendered body (terms replaced with metadata),
    sections, and referenced terms.
    """
    sections        = SectionSerializer(many=True, read_only=True)
    referenced_terms = serializers.SerializerMethodField()
    rendered_body   = serializers.SerializerMethodField()

    class Meta:
        model  = Article
        fields = ['id', 'title', 'subtitle', 'slug', 'rendered_body',
                'sections', 'referenced_terms', 'created_at']

    def get_referenced_terms(self, obj):
        """Extract all [[term_slug]] patterns and return their data."""
        import re
        slugs = re.findall(r'\[\[(\w+)\]\]', obj.body)
        terms = Term.objects.filter(slug__in=slugs).select_related('media_item')
        return TermSerializer(terms, many=True, context=self.context).data

    def get_rendered_body(self, obj):
        """
        Replace [[term_slug]] with a JSON-friendly marker so the
        frontend can inject clickable <span> elements.
        Format: __TERM:slug__
        """
        import re
        # First, escape any HTML in the body
        body_text = obj.body
        # Replace line breaks with <br>
        body_text = body_text.replace('\n', '<br>')
        # Replace [[term_slug]] with markers
        return re.sub(
            r'\[\[(\w+)\]\]',
            r'__TERM:\1__',
            body_text
        )