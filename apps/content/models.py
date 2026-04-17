from django.db import models
from django.utils.text import slugify


class MediaItem(models.Model):
    """
    Represents a multimedia asset: text, image, audio, video, or YouTube.
    """
    class MediaType(models.TextChoices):
        TEXT  = 'text',    'Text'
        IMAGE = 'image',   'Image'
        AUDIO = 'audio',   'Audio'
        VIDEO = 'video',   'Video (Local)'
        YOUTUBE = 'youtube', 'YouTube'

    title       = models.CharField(max_length=200)
    media_type  = models.CharField(max_length=20, choices=MediaType.choices)
    description = models.TextField(blank=True)          # For TEXT type
    file        = models.FileField(
                    upload_to='media_files/',
                    blank=True, null=True               # For IMAGE, AUDIO, VIDEO
                )
    youtube_url = models.URLField(blank=True, null=True) # For YOUTUBE type
    article     = models.ForeignKey(
                    'Article',
                    on_delete=models.CASCADE,
                    related_name='media_items',
                    null=True, blank=True               # Optional for flexibility
                )
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.media_type})"

    def clean(self):
        """Validate that the correct fields are filled per media_type."""
        from django.core.exceptions import ValidationError
        if self.media_type == self.MediaType.YOUTUBE:
            if not self.youtube_url:
                raise ValidationError("YouTube URL is required for YouTube media type.")
            # Ensure YouTube URL has a scheme (http or https)
            url = self.youtube_url.strip()
            if not url.startswith(('http://', 'https://', '//')):
                self.youtube_url = 'https://' + url
        if self.media_type in [self.MediaType.IMAGE, self.MediaType.AUDIO, self.MediaType.VIDEO]:
            if not self.file:
                raise ValidationError(f"File is required for {self.media_type} type.")


class Article(models.Model):
    """
    A news article or teaching content piece.
    """
    title      = models.CharField(max_length=300)
    subtitle   = models.CharField(max_length=500, blank=True, help_text="Short subtitle for the article")
    slug       = models.SlugField(unique=True, blank=True)
    body       = models.TextField(help_text="Use [[term_slug]] to mark interactive terms.")
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Section(models.Model):
    """
    Expandable accordion section belonging to an Article.
    E.g. Introduction, Detailed Explanation, Additional Resources.
    """
    class SectionType(models.TextChoices):
        INTRODUCTION  = 'introduction',  'Introduction'
        DETAILED      = 'detailed',      'Detailed Explanation'
        RESOURCES     = 'resources',     'Additional Resources'

    article      = models.ForeignKey(Article, related_name='sections', on_delete=models.CASCADE)
    section_type = models.CharField(max_length=30, choices=SectionType.choices)
    title        = models.CharField(max_length=200)
    content      = models.TextField()
    order        = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.article.title} - {self.title}"


class Term(models.Model):
    """
    A highlighted/clickable term in article body text.
    Links to a MediaItem for popup content.
    """
    slug       = models.SlugField(unique=True)
    label      = models.CharField(max_length=100, help_text="Display text in the article")
    media_item = models.ForeignKey(
                    MediaItem,
                    on_delete=models.SET_NULL,
                    null=True, blank=True,
                    related_name='terms'
                )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label


class MediaInteraction(models.Model):
    """
    Tracks when users interact with multimedia content.
    Used for analytics and engagement metrics.
    """
    media_item = models.ForeignKey(
        MediaItem,
        on_delete=models.CASCADE,
        related_name='interactions'
    )
    user_agent = models.TextField(blank=True, help_text="Browser/device info")
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    timestamp  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['media_item', '-timestamp']),
            models.Index(fields=['-timestamp']),
        ]

    def __str__(self):
        return f"{self.media_item.title} - {self.timestamp}"