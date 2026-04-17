from django.contrib import admin
from django.utils.html import format_html
from .models import MediaItem, Article, Section, Term, MediaInteraction


@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display  = ['title', 'media_type_badge', 'article', 'interaction_count', 'created_at']
    list_filter   = ['media_type', 'article', 'created_at']
    search_fields = ['title', 'description', 'article__title']
    readonly_fields = ['created_at', 'interaction_count']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'media_type', 'description', 'article', 'created_at')
        }),
        ('Media Content', {
            'fields': ('file', 'youtube_url'),
            'classes': ('collapse',)
        }),
        ('Analytics', {
            'fields': ('interaction_count',),
            'classes': ('collapse',)
        }),
    )
    
    def media_type_badge(self, obj):
        """Display media type as a colored badge."""
        colors = {
            'text': '#0dcaf0',
            'image': '#198754',
            'audio': '#6f42c1',
            'video': '#dc3545',
            'youtube': '#fd7e14',
        }
        color = colors.get(obj.media_type, '#6c757d')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 8px; border-radius: 3px;">{}</span>',
            color,
            obj.get_media_type_display()
        )
    media_type_badge.short_description = 'Media Type'
    
    def interaction_count(self, obj):
        """Display count of user interactions."""
        count = obj.interactions.count()
        return format_html('<strong>{}</strong> interactions', count)
    interaction_count.short_description = 'User Interactions'


class SectionInline(admin.TabularInline):
    model  = Section
    extra  = 1
    fields = ['section_type', 'title', 'content', 'order']
    ordering = ['order']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display   = ['title', 'slug', 'status_badge', 'section_count', 'created_at']
    list_filter    = ['is_active', 'created_at']
    search_fields  = ['title', 'body']
    inlines        = [SectionInline]
    readonly_fields = ['created_at', 'updated_at', 'slug']
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'subtitle', 'is_active')
        }),
        ('Content', {
            'fields': ('body',),
            'description': 'Use [[term_slug]] to mark interactive terms'
        }),
        ('Metadata', {
            'fields': ('slug', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def status_badge(self, obj):
        """Display article status as a colored badge."""
        if obj.is_active:
            return format_html(
                '<span style="background-color: #198754; color: white; padding: 3px 8px; border-radius: 3px;">Active</span>'
            )
        return format_html(
            '<span style="background-color: #6c757d; color: white; padding: 3px 8px; border-radius: 3px;">Inactive</span>'
        )
    status_badge.short_description = 'Status'
    
    def section_count(self, obj):
        """Display count of sections."""
        count = obj.sections.count()
        return format_html('<strong>{}</strong> section{}', count, 's' if count != 1 else '')
    section_count.short_description = 'Sections'


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display  = ['label', 'slug', 'media_item', 'term_badge', 'created_at']
    list_filter   = ['created_at', 'media_item__media_type']
    search_fields = ['label', 'slug', 'media_item__title']
    prepopulated_fields = {'slug': ('label',)}
    autocomplete_fields = ['media_item']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Term Information', {
            'fields': ('label', 'slug', 'media_item', 'created_at')
        }),
    )
    
    def term_badge(self, obj):
        """Display media type badge for the linked media item."""
        if obj.media_item:
            colors = {
                'text': '#0dcaf0',
                'image': '#198754',
                'audio': '#6f42c1',
                'video': '#dc3545',
                'youtube': '#fd7e14',
            }
            color = colors.get(obj.media_item.media_type, '#6c757d')
            return format_html(
                '<span style="background-color: {}; color: white; padding: 3px 8px; border-radius: 3px;">{}</span>',
                color,
                obj.media_item.get_media_type_display()
            )
        return '-'
    term_badge.short_description = 'Media Type'


@admin.register(MediaInteraction)
class MediaInteractionAdmin(admin.ModelAdmin):
    list_display  = ['media_item', 'timestamp', 'ip_address', 'user_agent_preview']
    list_filter   = ['timestamp', 'media_item']
    search_fields = ['media_item__title', 'ip_address']
    readonly_fields = ['media_item', 'user_agent', 'ip_address', 'timestamp']
    date_hierarchy = 'timestamp'
    
    def has_add_permission(self, request):
        # Users cannot manually add interactions - they're tracked automatically
        return False
    
    def has_delete_permission(self, request, obj=None):
        # Only superusers can delete interaction records
        return request.user.is_superuser
    
    def user_agent_preview(self, obj):
        """Display first 50 chars of user agent."""
        preview = obj.user_agent[:50] + '...' if len(obj.user_agent) > 50 else obj.user_agent
        return preview
    user_agent_preview.short_description = 'User Agent'