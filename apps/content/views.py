from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import MediaItem, Article, Term, MediaInteraction
from .serializers import (
    MediaItemSerializer,
    ArticleListSerializer,
    ArticleDetailSerializer,
    TermSerializer,
)


class MediaItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    GET /api/media-items/        → list all media items
    GET /api/media-items/{id}/   → retrieve single item (used for modal popup)
    POST /api/media-items/{id}/track/ → track user interaction
    """
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(detail=True, methods=['post'], url_path='track')
    def track(self, request, pk=None):
        """
        POST /api/media-items/{id}/track/
        Track user interaction with multimedia content for analytics.
        """
        media_item = self.get_object()
        
        # Get user agent and IP address
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip_address = x_forwarded_for.split(',')[0].strip() if x_forwarded_for else request.META.get('REMOTE_ADDR')
        
        # Create interaction record
        MediaInteraction.objects.create(
            media_item=media_item,
            user_agent=user_agent,
            ip_address=ip_address
        )
        
        return Response({'status': 'interaction tracked'}, status=status.HTTP_201_CREATED)


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    GET /api/articles/           → list articles
    GET /api/articles/{slug}/    → full article with sections + terms
    """
    queryset         = Article.objects.filter(is_active=True)
    lookup_field     = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ArticleDetailSerializer
        return ArticleListSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(detail=True, methods=['get'], url_path='sections')
    def sections(self, request, slug=None):
        """
        GET /api/articles/{slug}/sections/
        Returns only the expandable sections for an article.
        """
        article = self.get_object()
        from .serializers import SectionSerializer
        serializer = SectionSerializer(
            article.sections.all(), many=True
        )
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='media-items')
    def media_items(self, request, slug=None):
        """
        GET /api/articles/{slug}/media-items/
        Returns all media items linked to an article, optionally filtered by type.
        Query params: media_type=text|image|audio|video|youtube
        """
        article = self.get_object()
        media_type = request.query_params.get('media_type')
        
        queryset = article.media_items.all()
        if media_type:
            queryset = queryset.filter(media_type=media_type)
        
        serializer = MediaItemSerializer(
            queryset, many=True, context=self.get_serializer_context()
        )
        return Response(serializer.data)


class TermDetailView(generics.RetrieveAPIView):
    """
    GET /api/terms/{slug}/
    Returns term + its media item data for the modal popup.
    """
    queryset         = Term.objects.select_related('media_item')
    serializer_class = TermSerializer
    lookup_field     = 'slug'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context