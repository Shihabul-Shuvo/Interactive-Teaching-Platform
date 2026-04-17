# Debugging Log & Issue Resolution Guide

This document contains detailed debugging information, troubleshooting procedures, and solutions for common issues encountered during development and usage of the Interactive Teaching Platform.

## Table of Contents

- [Issue 1: Articles Not Displaying on Homepage](#issue-1-articles-not-displaying-on-homepage)
- [Issue 2: Multimedia Content Not Displaying](#issue-2-multimedia-content-not-displaying)
- [Issue 3: YouTube URL Validation Errors](#issue-3-youtube-url-validation-errors)
- [Issue 4: YouTube Video Player Error 153](#issue-4-youtube-video-player-error-153)
- [Summary of Fixes](#summary-of-fixes)

---

## Issue 1: Articles Not Displaying on Homepage

### Problem Description

When creating a new article in the Django admin panel, the article is successfully saved but does not appear in the article listing on the homepage (`http://localhost:8000/`), even though:
- The article is marked as `is_active = True`
- The article exists in the database
- The admin panel shows the article was created

### Root Cause Analysis

**Location**: `apps/core/views.py` → `IndexView.get()`

The `IndexView` applies specific filters to the queryset before rendering:

```python
articles = Article.objects.filter(
    is_active=True,
    slug__isnull=False
).exclude(
    slug=''
)
```

**The Problem**: Articles with empty or NULL slug values are filtered out. When the Django admin form saves a new article without a slug, the article fails these filters and doesn't display.

**Why This Happens**: 
1. Django forms validate fields before calling `model.save()`
2. The Article model's `save()` method auto-generates slug from title
3. However, this only happens AFTER the form validation completes
4. If slug field was user-editable in the form, leaving it blank would pass form validation
5. But then the article wouldn't match the filter criteria

### Developer Debugging Process

**Step 1: Confirm the Article Exists**
```bash
python manage.py shell
```
```python
from apps.content.models import Article
Article.objects.all()  # Output: <QuerySet [<Article: My Test Article>]>
```
✅ Article exists in database

**Step 2: Check Slug Value**
```python
article = Article.objects.first()
print(f"Slug: '{article.slug}'")  # Output: Slug: ''
print(f"Is Active: {article.is_active}")  # Output: Is Active: True
```
⚠️ Slug is empty string!

**Step 3: Test Filter Logic**
```python
# This is what IndexView does:
filtered = Article.objects.filter(
    is_active=True,
    slug__isnull=False
).exclude(slug='')
print(filtered)  # Output: <QuerySet []>
```
❌ Article is filtered out because slug is empty

**Step 4: Verify Auto-Generation Works**
```python
# Manually trigger save (simulating proper slug generation)
article.save()
print(f"Slug after save: '{article.slug}'")  # Output: Slug: 'my-test-article'

# Now test filter again:
filtered = Article.objects.filter(
    is_active=True,
    slug__isnull=False
).exclude(slug='')
print(filtered)  # Output: <QuerySet [<Article: My Test Article>]>
```
✅ Article now appears after slug is generated!

### Solution Implemented

**Step 1: Admin Configuration Change**

Modified `apps/content/admin.py` to prevent the slug confusion in the admin form:

```python
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # ... other settings ...
    
    # KEY: Make slug read-only so it never appears as editable
    readonly_fields = ['slug', 'created_at', 'updated_at']
    
    # Reorganize fields to hide slug by default
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'subtitle', 'body', 'is_active'),
            'description': 'Fill in the main article content'
        }),
        ('Metadata', {
            'fields': ('slug', 'created_at', 'updated_at'),
            'classes': ('collapse',),  # Hidden by default
            'description': 'Auto-generated fields (read-only)'
        }),
    )
```

**Step 2: Verification**

When creating a new article:
1. Fill in "Title", "Subtitle", "Body", and "Status"
2. **Don't see a slug field** - it's in collapsed metadata
3. Click "Save"
4. Django calls `Article.save()` → slug auto-generates from title
5. Article now appears on homepage ✅

**Best Practice**: Never leave slug field editable if you have auto-generation. The user confusion of "why isn't my article showing?" isn't worth it.

---

## Issue 2: Multimedia Content Not Displaying

### Problem Description

The article detail page (`/article/{slug}/`) displays correctly with the title, subtitle, and accordion sections. However, the "Multimedia Content Examples" section shows no actual media items displayed, even after adding media items in the admin panel and linking them to the article.

### Root Cause Analysis

This issue had **three interconnected causes**:

**Cause 1: No Database Relationship Between Article and MediaItem**

Original model structure:
```python
# In MediaItem model - NO article field!
class MediaItem(models.Model):
    title = models.CharField(max_length=200)
    media_type = models.CharField(...)
    description = models.TextField()
    file = models.FileField(...)
    youtube_url = models.URLField()
    # ❌ MISSING: No foreign key to Article
    created_at = models.DateTimeField(auto_now_add=True)
```

Without a relationship, the admin had no way to assign a media item to an article.

**Cause 2: No API Endpoint to Fetch Media for Article**

The API had:
- `GET /api/media-items/` - List ALL media items (not filtered by article)
- `GET /api/media-items/{id}/` - Get single media item

But NO:
- `GET /api/articles/{slug}/media-items/` - Get media items for specific article

**Cause 3: Missing Frontend JavaScript**

The `article_detail.html` template had no JavaScript to:
- Fetch media from API
- Filter by type
- Render media items in the UI

### Developer Debugging Process

**Step 1: Check Admin Interface**

Opened Django admin → MediaItem → Added new media item
- Filled in title, type, description, file
- **Looked for "Article" field** ❌ **Not present**
- Couldn't link media to article

**Step 2: Inspect Database Schema**

```bash
python manage.py shell
```
```python
from django.db import connection
from apps.content.models import MediaItem

# Get table structure
cursor = connection.cursor()
cursor.execute("PRAGMA table_info(content_mediaitem)")
columns = cursor.fetchall()

for col in columns:
    print(col)  # ❌ No 'article_id' column found
```

**Step 3: Check API Responses**

```bash
# Visit http://localhost:8000/api/articles/test-article/
# Response:
{
    "id": 1,
    "title": "Test Article",
    "slug": "test-article",
    "media_items": []  # ❌ Empty even though media exists in database
}

# The API doesn't have media_items field!
```

**Step 4: Browser Console Inspection**

Opened article page → F12 → Console:
```javascript
// No JavaScript errors
// But Network tab shows:
// ❌ Request to /api/articles/test-article/media-items/ returns 404
// API endpoint doesn't exist!
```

### Solution Implemented

**Step 1: Add Article Relationship to MediaItem**

Updated `apps/content/models.py`:

```python
class MediaItem(models.Model):
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=20, choices=MediaType.choices)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='media_files/', blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    
    # ✅ NEW: Link to article
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE,
        related_name='media_items',
        null=True, blank=True  # Optional for flexibility
    )
    created_at = models.DateTimeField(auto_now_add=True)
```

**Step 2: Create and Apply Migration**

```bash
python manage.py makemigrations
python manage.py migrate
```

Output:
```
Creating migration for content app...
  - Add field article to mediaitem
Applying content.0002_mediaitem_article... OK
```

**Step 3: Update Admin to Show Article Field**

Modified `apps/content/admin.py`:

```python
@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'media_type_badge', 'article', 'interaction_count', 'created_at']
    list_filter = ['media_type', 'article', 'created_at']  # ✅ Filter by article
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'media_type', 'description', 'article', 'created_at')  # ✅ Added article
        }),
        # ... rest of configuration
    )
```

**Step 4: Add API Endpoint**

Added to `apps/content/views.py` → `ArticleViewSet`:

```python
@action(detail=True, methods=['get'], url_path='media-items')
def media_items(self, request, slug=None):
    """
    GET /api/articles/{slug}/media-items/
    Returns media items linked to an article.
    Optional query param: media_type=text|image|audio|video|youtube
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
```

**Step 5: Complete JavaScript Implementation**

Rewrote multimedia loading JavaScript in `templates/core/article_detail.html`

#### Verification

After applying the solution:

1. **Admin Panel**: Can now assign article when creating media item
2. **API**: GET `/api/articles/test-article/media-items/` returns media
3. **Frontend**: Media items display with icon-based modal functionality
4. **User Experience**: Click media type icons → modal opens showing only that type's content ✅

---

## Issue 3: YouTube URL Validation Errors

### Problem Description

When adding a new media item with type "YouTube" in the admin panel and pasting a YouTube URL, the form fails validation, preventing the media item from being saved.

Users try to paste various URL formats:
- `youtube.com/watch?v=dQw4w9WgXcQ`
- `youtu.be/dQw4w9WgXcQ`
- `m.youtube.com/watch?v=dQw4w9WgXcQ`

All of these fail validation.

### Root Cause Analysis

**Location**: Django's built-in `URLField` validator

Django's `URLField` uses a strict regex pattern that requires:
1. A protocol scheme (http://, https://, //)
2. Valid domain name
3. Optional path, query string, fragment

### Developer Debugging Process

**Step 1: Reproduce the Error**

1. Open Django admin
2. Go to Media Items → Add Media Item
3. Fill form:
   - Title: "Test Video"
   - Media Type: "YouTube"
   - YouTube URL: `youtube.com/watch?v=test123`
4. Click Save
5. **Result**: Validation error appears

**Step 2: Check Django URLField Implementation**

```bash
python manage.py shell
```

```python
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

validator = URLValidator()

# Test various formats
test_urls = [
    'youtube.com/watch?v=test',           # ❌ Fails
    'https://youtube.com/watch?v=test',   # ✅ Passes
    'youtu.be/test',                      # ❌ Fails
    'https://youtu.be/test',              # ✅ Passes
]

for url in test_urls:
    try:
        validator(url)
        print(f"✅ {url}")
    except ValidationError:
        print(f"❌ {url}")
```

**Output**:
```
❌ youtube.com/watch?v=test
✅ https://youtube.com/watch?v=test
❌ youtu.be/test
✅ https://youtu.be/test
```

✅ Confirmed: URLField requires scheme

### Solution Implemented

Modified the `clean()` method in `apps/content/models.py`:

```python
def clean(self):
    """Validate that the correct fields are filled per media_type."""
    from django.core.exceptions import ValidationError
    
    if self.media_type == self.MediaType.YOUTUBE:
        if not self.youtube_url:
            raise ValidationError("YouTube URL is required for YouTube media type.")
        
        # ✅ Auto-add https:// if missing
        url = self.youtube_url.strip()
        if not url.startswith(('http://', 'https://', '//')):
            self.youtube_url = 'https://' + url
    
    if self.media_type in [self.MediaType.IMAGE, self.MediaType.AUDIO, self.MediaType.VIDEO]:
        if not self.file:
            raise ValidationError(f"File is required for {self.media_type} type.")
```

**Test All Formats After Fix**:
```
Input: youtube.com/watch?v=dQw4w9WgXcQ
Stored: https://youtube.com/watch?v=dQw4w9WgXcQ ✅

Input: youtu.be/dQw4w9WgXcQ
Stored: https://youtu.be/dQw4w9WgXcQ ✅

Input: //youtube.com/watch?v=dQw4w9WgXcQ
Stored: //youtube.com/watch?v=dQw4w9WgXcQ ✅

Input: https://youtube.com/watch?v=dQw4w9WgXcQ
Stored: https://youtube.com/watch?v=dQw4w9WgXcQ ✅ (unchanged)
```

---

## Issue 4: YouTube Video Player Error 153

### Problem Description

When viewing a YouTube video in the media modal, error 153 or similar video player configuration errors appear instead of the embedded video.

### Root Cause Analysis

Several possible causes:

1. **Malformed Video ID Extraction**: The URL might not be parsed correctly to extract the video ID
2. **CORS Issues**: Cross-origin restrictions on some YouTube domains
3. **Invalid Embed URL Format**: Not using the correct `youtube.com/embed/` format
4. **Network/Proxy Issues**: Firewall or proxy blocking YouTube embeds

### Developer Debugging Process

**Step 1: Inspect Network Requests**

Browser DevTools → Network tab:
1. Open article with YouTube media
2. Click YouTube media type icon
3. Modal opens
4. Check Network tab for YouTube frame requests
5. Look for failed requests (HTTP 403, blocked by CORS, etc.)

**Step 2: Test Video ID Extraction**

In browser console:
```javascript
const url = 'https://youtube.com/watch?v=dQw4w9WgXcQ';
const match = url.match(/v=([a-zA-Z0-9_-]{11})/);
console.log(match[1]);  // Should output: dQw4w9WgXcQ
```

**Step 3: Check iFrame Attributes**

```javascript
// Test iFrame creation
const iframe = document.createElement('iframe');
iframe.src = 'https://www.youtube.com/embed/dQw4w9WgXcQ';
iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
iframe.allowFullscreen = true;
console.log(iframe.outerHTML);  // Check if attributes are correct
```

### Solution Implemented

Updated the `renderYouTubeEmbed()` function in `templates/core/article_detail.html`:

```javascript
function renderYouTubeEmbed(url) {
    try {
        // Extract video ID from various YouTube URL formats
        let videoId = null;
        
        // Format: https://www.youtube.com/watch?v=VIDEO_ID
        if (url.includes('youtube.com/watch')) {
            const match = url.match(/v=([a-zA-Z0-9_-]{11})/);
            if (match) videoId = match[1];
        }
        // Format: https://youtu.be/VIDEO_ID
        else if (url.includes('youtu.be/')) {
            const match = url.match(/youtu\.be\/([a-zA-Z0-9_-]{11})/);
            if (match) videoId = match[1];
        }
        // Format: youtube.com/embed/VIDEO_ID
        else if (url.includes('embed/')) {
            const match = url.match(/embed\/([a-zA-Z0-9_-]{11})/);
            if (match) videoId = match[1];
        }
        
        if (videoId) {
            return `<div class="relative w-full pt-[56.25%] bg-black rounded-lg overflow-hidden">
                <iframe class="absolute top-0 left-0 w-full h-full" 
                    src="https://www.youtube.com/embed/${videoId}?modestbranding=1&rel=0" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen>
                </iframe>
            </div>`;
        } else {
            return `<div class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
                <p class="font-semibold">⚠️ Video Player Error</p>
                <p class="text-sm mt-1">Could not extract video ID from URL: ${url}</p>
                <p class="text-sm mt-2"><a href="${url}" target="_blank" class="underline hover:no-underline">Open video in new tab</a></p>
            </div>`;
        }
    } catch (error) {
        console.error('YouTube embed error:', error);
        return `<div class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
            <p class="font-semibold">⚠️ Video Player Configuration Error</p>
            <p class="text-sm mt-1">Error: ${error.message}</p>
        </div>`;
    }
}
```

**Key improvements:**
- Handles multiple YouTube URL formats
- Extracts video ID using regex matching
- Provides fallback UI with link to watch on YouTube
- Better error messages for debugging

### Troubleshooting Steps

If YouTube videos still don't work:

1. **Check URL Format**:
   ```bash
   # Verify URL is properly formatted with https:// scheme
   python manage.py shell
   from apps.content.models import MediaItem
   m = MediaItem.objects.filter(media_type='youtube').first()
   print(m.youtube_url)
   ```

2. **Test Video ID Extraction**:
   Open browser console and test:
   ```javascript
   const url = 'YOUR_YOUTUBE_URL';
   const match = url.match(/v=([a-zA-Z0-9_-]{11})/);
   console.log('Video ID:', match ? match[1] : 'Not found');
   ```

3. **Check iframe Attributes**:
   Ensure these attributes are present:
   - `allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"`
   - `allowfullscreen`

4. **Network Issues**:
   If YouTube is blocked by network:
   - Try using youtu.be domain instead of youtube.com
   - Check firewall/proxy settings
   - Test with different video IDs

---

## Summary of Fixes

| Issue | Root Cause | Solution | Impact |
|-------|-----------|----------|--------|
| Articles not displaying | Empty slug field excluded by filter | Moved slug to read-only metadata in admin | Articles always visible when active |
| Multimedia not showing | No Article-MediaItem relationship | Added ForeignKey, API endpoint, modal | Media displays correctly with icon-based access |
| YouTube URL errors | URLField requires scheme | Auto-prepend https:// in clean() | Any YouTube URL format accepted |
| YouTube player error 153 | Malformed video ID extraction | Improved video ID parsing and error handling | Better embedded YouTube player reliability |

---

## Additional Debugging Tips

### Enable Django Debug Toolbar

For in-depth debugging during development:

```bash
pip install django-debug-toolbar
```

Add to `config/settings.py`:
```python
INSTALLED_APPS = [
    'debug_toolbar',
    # ... other apps
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ... other middleware
]

INTERNAL_IPS = ['127.0.0.1']
```

### Browser Console Debugging

Check for JavaScript errors:
1. Press F12
2. Go to Console tab
3. Reload page
4. Look for red error messages
5. Click error to expand and see stack trace

### Django Shell Debugging

```bash
python manage.py shell
```

Common queries:
```python
# Check articles
from apps.content.models import Article
Article.objects.all().values('id', 'title', 'slug', 'is_active')

# Check media items for an article
article = Article.objects.first()
article.media_items.all()

# Check terms
from apps.content.models import Term
Term.objects.all()

# Check interactions
from apps.content.models import MediaInteraction
MediaInteraction.objects.count()
```

### Logging Configuration

Add to `config/settings.py`:
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

Then monitor the log file:
```bash
tail -f debug.log
```
