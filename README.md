# Interactive Teaching Platform

A professional-grade Django 5.2.7 web application for multimedia-rich interactive learning. This platform demonstrates full-stack web development with modern best practices including REST API design, responsive UI/UX, database optimization, and comprehensive content management.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Setup Instructions](#setup-instructions)
- [Core Features](#core-features)
- [Database Schema](#database-schema)
- [API Documentation](#api-documentation)
- [Key Implementation Details](#key-implementation-details)
- [Troubleshooting Guide](#troubleshooting-guide)
- [Performance Optimization](#performance-optimization)
- [Future Enhancements](#future-enhancements)

---

## Project Overview

### Purpose and Design

The Interactive Teaching Platform is engineered to bridge the gap between traditional content delivery and interactive learning experiences. Built with Django and modern frontend technologies, it provides:

- **Content Creators**: Intuitive admin interface with slug auto-generation, rich-text editing, and multimedia management
- **Learners**: Responsive interface with interactive terms, expandable sections, and multimedia content discovery
- **Administrators**: Comprehensive analytics tracking, content filtering, and performance monitoring

### Core Capabilities

✨ **Content Management**
- Dynamic article creation with auto-generated SEO-friendly slugs
- Interactive term linking to multimedia content
- Structured sections (introduction, detailed explanation, resources)
- Multi-language support (demonstrated with Bengali content)

🎯 **Interactive Features**
- Clickable terms with dotted underline styling
- Modal-based multimedia content display (images, videos, audio, text)
- Expandable accordion sections with smooth CSS transitions
- Real-time interaction analytics tracking

📱 **Responsive Design**
- Mobile-first Tailwind CSS approach
- Desktop, tablet, and mobile optimization
- Touch-friendly interface elements
- Cross-browser compatibility

---

## Architecture

### System Design

```
┌──────────────────────────────────────────────────────────────────┐
│                          Client Layer                             │
│  HTML5 + Tailwind CSS + Vanilla ES6+ JavaScript + FontAwesome    │
│  - Article listing (responsive grid)                              │
│  - Article detail with interactive elements                       │
│  - Multimedia modal (type-aware display)                          │
│  - Accordion sections (CSS height transitions)                    │
└──────────────────────────────────────────────────────────────────┘
                              ↓ REST API Calls (JSON)
┌──────────────────────────────────────────────────────────────────┐
│                  Django REST Framework Layer                      │
│  ViewSets, Serializers, Permissions, Pagination                  │
│  - GET /api/articles/{slug}/     → Article with rendered_body    │
│  - GET /api/media-items/{id}/    → Multimedia content            │
│  - POST /api/media-items/{id}/track/  → Interaction logging      │
└──────────────────────────────────────────────────────────────────┘
                              ↓ ORM Queries
┌──────────────────────────────────────────────────────────────────┐
│              Django Models & Business Logic                       │
│  - Article (with slug auto-generation)                            │
│  - MediaItem (type-validated)                                     │
│  - Section (ordered accordion content)                            │
│  - Term (interactive element linking)                             │
│  - MediaInteraction (analytics)                                   │
└──────────────────────────────────────────────────────────────────┘
                              ↓ Database Queries
┌──────────────────────────────────────────────────────────────────┐
│           SQLite3 (Development) / PostgreSQL (Production)         │
│  Relational schema with foreign keys and indexed fields           │
└──────────────────────────────────────────────────────────────────┘
```

### Key Design Patterns

**Model-View-Template (MVT) Pattern**:
- Models define data structure and business logic
- Views handle request/response and API endpoints
- Templates render HTML with Tailwind CSS classes

**Serializer Pattern**:
- Separate serializer classes for different API responses
- Automatic JSON conversion and validation
- Method fields for computed values (rendered_body)

**Admin Interface Pattern**:
- Custom ModelAdmin classes with fieldset organization
- Read-only fields for auto-generated and audit fields
- Inline editing for related objects (sections)

### Project File Structure

```
Interactive Teaching Platform/
├── manage.py                          # Django CLI entry point
├── requirements.txt                   # Python package dependencies
├── db.sqlite3                        # Development database
│
├── config/                           # Django configuration
│   ├── settings.py                  # Project-wide settings
│   ├── urls.py                      # Root URL routing
│   ├── asgi.py                      # ASGI application (async)
│   └── wsgi.py                      # WSGI application (production)
│
├── apps/
│   ├── core/                        # Frontend view rendering
│   │   ├── views.py                # IndexView, ArticleDetailView
│   │   ├── urls.py                 # Frontend URL patterns
│   │   └── migrations/
│   │
│   └── content/                     # API and data models
│       ├── models.py               # Article, MediaItem, Section, Term, MediaInteraction
│       ├── views.py                # ViewSets for REST API
│       ├── serializers.py          # DRF serializers
│       ├── admin.py                # Django admin customization
│       ├── urls.py                 # API routes (/api/...)
│       ├── apps.py                 # App configuration
│       ├── migrations/             # Database migrations
│       └── management/commands/    # Custom commands
│           └── load_nvidia_article.py
│
├── templates/
│   └── core/
│       ├── base.html               # Master template with Tailwind
│       ├── index.html              # Articles listing page
│       └── article_detail.html     # Single article detail page
│
└── static/
    ├── css/
    │   └── style.css               # Custom CSS and animations
    └── js/
        └── modal.js                # Modal state management
```

---

## Technology Stack

### Backend (Server-side)

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| Framework | Django | 5.2.7 | Web application framework |
| API | Django REST Framework | 3.15.1 | RESTful API endpoints |
| Database | SQLite3 | Built-in | Development database |
| ORM | Django ORM | Built-in | Database queries and relationships |
| Admin | Django Admin | Built-in | Content management interface |

### Frontend (Client-side)

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| Markup | HTML5 | - | Semantic page structure |
| Styling | Tailwind CSS | 3.x (CDN) | Utility-first CSS framework |
| Icons | FontAwesome | 6.4.0 | Icon library (search, close, etc.) |
| JavaScript | Vanilla ES6+ | - | Modal management, term rendering |
| HTTP | Fetch API | Built-in | REST API communication |

### Infrastructure

| Component | Technology | Notes |
|-----------|-----------|-------|
| Development Server | Django runserver | localhost:8000 |
| Static Files | Django staticfiles | CSS, JS, icons |
| Media Files | FileField storage | Local file system |
| Version Control | Git | Recommended for production |

### Security Components

- **CSRF Protection**: Django middleware + X-CSRFToken header validation
- **SQL Injection Prevention**: ORM parameterized queries
- **XSS Prevention**: Django template auto-escaping
- **Authentication**: Django's built-in session/auth (extensible)

---

## Setup Instructions

### Prerequisites

- **Python**: 3.11 or higher
- **pip**: Python package manager
- **Virtual Environment**: Strongly recommended for isolation

### Step-by-Step Installation

#### 1. Navigate to project directory
```bash
cd "g:\Job test\Interactive Teaching Platform"
```

#### 2. Create virtual environment (optional but recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Linux/Mac
python -m venv venv
source venv/bin/activate
```

#### 3. Install dependencies
```bash
pip install -r requirements.txt
```

#### 4. Run database migrations
```bash
python manage.py migrate
```
This creates the SQLite database and applies all migrations.

#### 5. Create superuser account
```bash
python manage.py createsuperuser
```
Follow the prompts to create admin credentials.

#### 6. Load sample data (optional)
```bash
python manage.py load_nvidia_article
```
Loads a comprehensive Bengali-language article about Nvidia Physical AI with multimedia content.

#### 7. Start development server
```bash
python manage.py runserver
```

### Access Points

- **Frontend**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/
- **API Root**: http://localhost:8000/api/
- **API Documentation**: http://localhost:8000/api/ (DRF browsable API)

---

## Core Features

### 1. Article Management

**Auto-Generated Slugs**:
- Slugs automatically generated from article title
- Handles non-ASCII characters (e.g., Bengali script)
- Ensures unique slugs for clean URLs

**Rich-Text Content**:
- Support for interactive term markup using `[[term_slug]]` syntax
- Converted to `__TERM:term_slug__` in rendered output
- Frontend JavaScript replaces markers with clickable buttons

**Content Control**:
- `is_active` boolean field for publication status
- Created/updated timestamps for audit trail
- Version tracking ready for future enhancements

### 2. Interactive Terms

**User Interaction Pattern**:
1. User hovers over dotted-underline term text
2. Cursor changes to indicate clickability
3. Click opens modal with linked multimedia content
4. Interaction recorded to analytics database

**Technical Implementation**:
- ForeignKey linking Term to MediaItem
- Slug-based URL routing (`/api/terms/{slug}/`)
- Frontend fetch and modal display

### 3. Multimedia Content Management

**Supported Media Types**:

| Type | Storage | Display | Use Case |
|------|---------|---------|----------|
| Text | TextField | Direct rendering in modal | Definitions, explanations |
| Image | FileField | Responsive img tag | Photos, diagrams, illustrations |
| Audio | FileField | HTML5 audio player | Narration, pronunciation |
| Video | FileField | HTML5 video player | Demonstrations, tutorials |
| YouTube | URL field | Embedded iframe | External video content |

**Type Validation**:
- Custom `clean()` method validates media-type-specific fields
- Example: YouTube type requires valid YouTube URL
- Prevents invalid data creation

### 4. Expandable Accordion Sections

**Section Types**:
- **Introduction**: Introductory overview of topic
- **Detailed Explanation**: In-depth technical content
- **Additional Resources**: Links and supplementary material

**Interaction**:
- Click section header to toggle open/close
- Chevron icon rotates indicating state
- Content smoothly expands with CSS max-height transition
- Multiple sections can be open simultaneously

**Technical Details**:
- Ordered by `order` field for consistent display
- `whitespace-pre-wrap` preserves formatting
- `max-h-0` to `max-h-96` transition in 300ms

### 5. Analytics Tracking

**Tracked Events**:
- User clicks on interactive term
- Click triggers `/api/media-items/{id}/track/` endpoint
- Creates MediaInteraction record with:
  - Timestamp
  - Media item referenced
  - User's IP address (optional)
  - User agent string

**Admin Display**:
- Interaction count displayed in MediaItem admin list
- Filterable by media type and date
- Quick insight into content engagement

---

## Database Schema

### Entity Relationship Diagram

```
┌────────────────────────────────────────────────────────────┐
│                     Article                                │
├────────────────────────────────────────────────────────────┤
│ id (PK)                                                    │
│ title (CharField, 300)                                     │
│ subtitle (CharField, 500, optional)                        │
│ slug (SlugField, unique, auto-generated)                   │
│ body (TextField) - contains [[term_slug]] markers          │
│ is_active (BooleanField, default=True)                     │
│ created_at (DateTimeField, auto)                           │
│ updated_at (DateTimeField, auto)                           │
└────────────────────────────────────────────────────────────┘
           │                          │
           │ (Reverse FK)             │
           │                          │
    ┌──────▼──────────┐      ┌────────▼──────────┐
    │    Section      │      │      Term         │
    ├─────────────────┤      ├───────────────────┤
    │ id (PK)         │      │ id (PK)           │
    │ article_id (FK) │      │ slug (SlugField)  │
    │ title           │      │ label             │
    │ section_type    │      │ media_item_id (FK)│
    │ content         │      │ created_at        │
    │ order           │      └───────────────────┘
    │ created_at      │              │
    │ updated_at      │              │ (ForeignKey)
    └─────────────────┘              │
                         ┌────────────▼──────────────┐
                         │      MediaItem           │
                         ├──────────────────────────┤
                         │ id (PK)                  │
                         │ title (CharField, 200)   │
                         │ media_type (choice field)│
                         │ description (TextField)  │
                         │ file (FileField, opt)    │
                         │ youtube_url (URLField)   │
                         │ created_at               │
                         └──────────────────────────┘
                                    │
                                    │ (Reverse FK)
                                    │
                         ┌──────────▼──────────────┐
                         │  MediaInteraction       │
                         ├──────────────────────────┤
                         │ id (PK)                 │
                         │ media_item_id (FK)      │
                         │ user_agent (CharField)  │
                         │ ip_address (IPField)    │
                         │ timestamp (DateTimeField)
                         └──────────────────────────┘
```

### Model Definitions

#### Article Model
```python
class Article(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=500, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()  # Contains [[term_slug]] markers
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        """Auto-generate slug from title if not provided"""
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug if base_slug else self._generate_random_slug()
        super().save(*args, **kwargs)
```

#### MediaItem Model
```python
class MediaItem(models.Model):
    MEDIA_TYPES = (
        ('text', 'Text'),
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('youtube', 'YouTube'),
    )
    
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPES)
    description = models.TextField()
    file = models.FileField(upload_to='media_files/', blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        """Validate media_type-specific fields"""
        if self.media_type == 'youtube' and not self.youtube_url:
            raise ValidationError("YouTube type requires youtube_url")
        if self.media_type in ['image', 'audio', 'video'] and not self.file:
            raise ValidationError(f"{self.media_type} type requires a file")
```

#### Section Model
```python
class Section(models.Model):
    SECTION_TYPES = (
        ('introduction', 'Introduction'),
        ('detailed', 'Detailed Explanation'),
        ('resources', 'Additional Resources'),
    )
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='sections')
    section_type = models.CharField(max_length=30, choices=SECTION_TYPES)
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveSmallIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
```

#### Term Model
```python
class Term(models.Model):
    slug = models.SlugField(unique=True)
    label = models.CharField(max_length=200)
    media_item = models.ForeignKey(MediaItem, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

#### MediaInteraction Model
```python
class MediaInteraction(models.Model):
    media_item = models.ForeignKey(MediaItem, on_delete=models.CASCADE, related_name='interactions')
    user_agent = models.CharField(max_length=500, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [models.Index(fields=['media_item', '-timestamp'])]
```

---

## API Documentation

### Endpoint Overview

All API endpoints are prefixed with `/api/`. The API returns JSON responses with appropriate HTTP status codes.

### 1. Articles Endpoints

#### List Articles
```
GET /api/articles/
```

**Query Parameters**:
- `page`: Page number (default: 1)
- `is_active`: Filter by status (true/false)

**Response** (200 OK):
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Article Title",
      "subtitle": "Subtitle here",
      "slug": "article-slug",
      "body": "Content with [[term_slug]] markers",
      "rendered_body": "Content with __TERM:term_slug__ markers",
      "is_active": true,
      "created_at": "2026-04-17T12:00:00Z",
      "updated_at": "2026-04-17T12:00:00Z",
      "sections": [...]
    }
  ]
}
```

#### Retrieve Article by Slug
```
GET /api/articles/{slug}/
```

**Response** (200 OK):
```json
{
  "id": 1,
  "title": "Article Title",
  "slug": "article-slug",
  "body": "Content with [[term_slug]] markers",
  "rendered_body": "Content with __TERM:term_slug__ markers",
  "is_active": true,
  "sections": [
    {
      "id": 1,
      "title": "Introduction",
      "section_type": "introduction",
      "content": "Section content here",
      "order": 0
    }
  ],
  "referenced_terms": [
    {
      "slug": "term_slug",
      "label": "Term Label",
      "media_item_id": 1
    }
  ],
  "created_at": "2026-04-17T12:00:00Z"
}
```

#### Get Article Sections
```
GET /api/articles/{slug}/sections/
```

**Response** (200 OK):
```json
{
  "article_slug": "article-slug",
  "sections": [
    {
      "id": 1,
      "title": "Introduction",
      "section_type": "introduction",
      "content": "...",
      "order": 0
    }
  ]
}
```

### 2. Media Items Endpoints

#### List Media Items
```
GET /api/media-items/
```

**Query Parameters**:
- `media_type`: Filter by type (text, image, audio, video, youtube)
- `page`: Page number

**Response** (200 OK):
```json
{
  "count": 10,
  "results": [
    {
      "id": 1,
      "title": "Media Title",
      "media_type": "image",
      "description": "Description text",
      "file_url": "http://localhost:8000/media/media_files/image.jpg",
      "youtube_url": null,
      "created_at": "2026-04-17T12:00:00Z",
      "interaction_count": 5
    }
  ]
}
```

#### Retrieve Media Item
```
GET /api/media-items/{id}/
```

**Response** (200 OK):
```json
{
  "id": 1,
  "title": "Media Title",
  "media_type": "image",
  "description": "Description",
  "file_url": "http://localhost:8000/media/...",
  "youtube_url": null,
  "created_at": "2026-04-17T12:00:00Z"
}
```

#### Track Media Interaction
```
POST /api/media-items/{id}/track/
```

**Request Body**:
```json
{
  "user_agent": "Mozilla/5.0...",
  "ip_address": "192.168.1.1"
}
```

**Response** (201 Created):
```json
{
  "id": 1,
  "media_item": 5,
  "timestamp": "2026-04-17T12:30:00Z",
  "user_agent": "Mozilla/5.0...",
  "ip_address": "192.168.1.1"
}
```

### 3. Terms Endpoints

#### Retrieve Term by Slug
```
GET /api/terms/{slug}/
```

**Response** (200 OK):
```json
{
  "id": 1,
  "slug": "term-slug",
  "label": "Term Display Label",
  "media_item": {
    "id": 5,
    "title": "Media Title",
    "media_type": "text",
    "description": "...",
    "file_url": null,
    "youtube_url": null
  },
  "created_at": "2026-04-17T12:00:00Z"
}
```

### Query Optimization Strategies

The API implements several optimization patterns:

```python
# Prefetch related to reduce database queries
articles = Article.objects.filter(
    is_active=True
).prefetch_related('sections')  # Fetches all sections in 1 query

# Select related for ForeignKey optimization
terms = Term.objects.select_related('media_item')
```

**Query Performance**:
- List endpoint: ~2 queries (1 articles + 1 sections via prefetch)
- Detail endpoint: ~2 queries (1 article + 1 sections)
- Pagination: Limits to 10 items per page

---

## Key Implementation Details

### 1. Slug Auto-Generation with Non-ASCII Support

**Challenge**: `slugify()` removes non-ASCII characters, potentially creating empty slugs.

**Solution Implemented**:
```python
# In Article.save()
if not self.slug:
    base_slug = slugify(self.title)  # Converts "ফিজিক্যাল এআই" → ""
    self.slug = base_slug if base_slug else self._generate_random_slug()
```

**Why This Matters**:
- Ensures every article has a valid, unique slug
- Maintains SEO-friendly URLs
- Gracefully handles international content (Bengali, Arabic, etc.)
- Fallback to random slug prevents data integrity issues

**Alternative Approach**:
Could use transliteration libraries (unidecode) to convert Bengali → Latin, but random slug provides cleaner fallback.

### 2. Interactive Term Rendering Pipeline

**Complete Data Flow**:

```
1. Content Storage (Backend)
   Article.body = "Explain [[omniverse]] concept"

2. Serialization (API Response)
   rendered_body = "Explain __TERM:omniverse__ concept"

3. Frontend Fetching
   fetch('/api/articles/my-article/')
   → JavaScript receives rendered_body

4. DOM Manipulation
   regex = /__TERM:(\w+)__/g
   Replaces with: <button class="term-button">label</button>

5. Event Binding
   button.onclick → fetch('/api/terms/{slug}/')
   → fetch multimedia → display in modal

6. Analytics
   Modal shown → POST /api/media-items/{id}/track/
   → Creates MediaInteraction record
```

**Technical Implementation**:
```javascript
// Frontend term replacement (article_detail.html)
const rendered = renderedBody.replace(/__TERM:(\w+)__/g, (match, slug) => {
    const term = terms.find(t => t.slug === slug);
    return `<button class="term-button" data-slug="${slug}">
        ${term.label} <i class="fas fa-search"></i>
    </button>`;
});

// Event delegation for term clicks
document.addEventListener('click', async (e) => {
    if (e.target.classList.contains('term-button')) {
        const slug = e.target.dataset.slug;
        const response = await fetch(`/api/terms/${slug}/`);
        const term = await response.json();
        displayMediaModal(term.media_item);
    }
});
```

**Why This Two-Step Process**:
- Database stores original markup for admin editing
- API provides ready-to-render output for frontend
- Prevents double-processing and regex complexity on frontend
- Clean separation of concerns

### 3. Modal State Management Without Framework Libraries

**Challenge**: Manage modal visibility, backdrop clicks, keyboard events without jQuery or React.

**Implementation** (static/js/modal.js):
```javascript
const multimediaModal = document.getElementById('multimediaModal');
const modalBackdrop = document.getElementById('modalBackdrop');
const modalClose = document.getElementById('modalClose');

function showModal(mediaItem) {
    // Set content based on media type
    if (mediaItem.media_type === 'image') {
        modalContent.innerHTML = `<img src="${mediaItem.file_url}" alt="${mediaItem.title}">`;
    } else if (mediaItem.media_type === 'youtube') {
        const videoId = extractYoutubeId(mediaItem.youtube_url);
        modalContent.innerHTML = `<iframe src="https://www.youtube.com/embed/${videoId}" ...></iframe>`;
    }
    
    // Show modal with CSS classes
    multimediaModal.classList.remove('hidden');
    setTimeout(() => modalBackdrop.classList.add('opacity-100'), 10);
}

function hideModal() {
    modalBackdrop.classList.remove('opacity-100');
    setTimeout(() => multimediaModal.classList.add('hidden'), 300);
}

// Event listeners
modalClose.addEventListener('click', hideModal);

// Backdrop click detection (only closes on backdrop, not content)
modalBackdrop.addEventListener('click', (e) => {
    if (e.target === modalBackdrop) hideModal();
});

// Keyboard support
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') hideModal();
});
```

**Design Decisions**:
- CSS classes handle visibility (not inline styles)
- `setTimeout` allows CSS transition timing
- Event delegation prevents bubbling issues
- No third-party dependencies

### 4. Accordion with Smooth CSS Height Transitions

**Challenge**: Smoothly animate expanding/collapsing content without knowing height in advance.

**Solution** (templates/core/article_detail.html):
```html
<!-- Collapsed by default: max-h-0 -->
<div class="accordion-content transition-all duration-300 max-h-0 overflow-hidden"
     data-section-id="{{ section.id }}">
    <div class="px-6 py-3 bg-gray-50 text-gray-700 whitespace-pre-wrap">
        {{ section.content }}
    </div>
</div>
```

```javascript
function setupAccordion() {
    document.querySelectorAll('.accordion-toggle').forEach(button => {
        button.addEventListener('click', function() {
            const content = this.nextElementSibling;
            const isOpen = content.classList.contains('max-h-0');
            
            if (isOpen) {
                // Opening: set max-h to scrollHeight
                const height = content.querySelector('div').scrollHeight;
                content.style.maxHeight = height + 'px';
                content.classList.remove('max-h-0');
            } else {
                // Closing: set max-h to 0
                content.classList.add('max-h-0');
                content.style.maxHeight = '0px';
            }
            
            // Rotate chevron icon
            const chevron = this.querySelector('.fa-chevron-down');
            chevron.style.transform = isOpen ? 'rotate(180deg)' : 'rotate(0deg)';
        });
    });
}
```

**Why `scrollHeight`**:
- Detects actual content height dynamically
- Works with variable content lengths
- No hardcoded pixel values needed
- Responsive to content changes

**CSS Transitions**:
```css
.accordion-content {
    transition: max-height 0.3s ease, opacity 0.3s ease;
}

/* Chevron rotation */
.accordion-toggle .fa-chevron-down {
    transition: transform 0.3s ease;
}
```

### 5. Admin Form Design with Auto-Generated Slugs

**Problem**: User-editable slug field causes validation errors when creating articles.

**Root Cause**: Django admin form validates all fields before `save()` is called, but slug is empty until `Article.save()` auto-generates it.

**Solution** (apps/content/admin.py):
```python
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    
    # Reorganized fieldsets to handle auto-generated slug
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'subtitle', 'body', 'is_active'),
            'description': 'Main article content and publication status'
        }),
        ('Metadata', {
            'fields': ('slug', 'created_at', 'updated_at'),
            'classes': ('collapse',),  # Hidden by default
            'description': 'Auto-generated fields (read-only)'
        }),
    )
    
    inlines = [SectionInline]
```

**Key Design Decision**: Remove slug from main fieldset entirely. Show it in collapsed metadata section for reference only.

**Alternative Approaches Considered**:
1. ❌ Make slug optional in form: Still shows in fieldset, confusing UX
2. ❌ Override form.__init__: Hacky, hard to maintain
3. ✅ Remove from fieldset + readonly_fields: Clean, clear intent

---

## Troubleshooting Guide

### Issue 1: Admin Article Add Form Shows "NoReverseMatch" Error

**Symptom**:
```
django.urls.exceptions.NoReverseMatch: 
Reverse for 'article-detail' with arguments... not found
```

**Root Cause**: 
- Form tries to generate admin "change" URL for new article
- Slug not yet auto-generated (happens in `save()`)
- URL lookup fails without slug

**Solution**:
1. In `ArticleAdmin`, remove slug from main fieldsets
2. Add slug to `readonly_fields`
3. Put slug in collapsed 'Metadata' fieldset
4. Django skips URL generation for collapsed fields

**Verification**:
- Add new article in admin without slug field in view
- Slug auto-generates on save
- Edit page shows slug in metadata section

### Issue 2: Accordion Content Has Large Blank Space Above Text

**Symptom**: 
When accordion section opens, text starts after significant empty space. Content appears to "fall down" into the accordion.

**Root Cause**:
```html
<!-- WRONG: padding too large + linebreaks filter adds extra breaks -->
<div class="px-6 py-4">
    {{ section.content | linebreaks }}
</div>
```

This combination creates:
1. Padding: `py-4` = 1rem (16px) top and bottom
2. Filter: `linebreaks` wraps each line in `<p>` tags
3. Result: Multiple line breaks before content starts

**Solution**:
```html
<!-- CORRECT: reduced padding + whitespace-pre-wrap preserves formatting -->
<div class="px-6 py-3 text-gray-700 whitespace-pre-wrap">
    {{ section.content }}
</div>
```

**Changes Made**:
- `py-4` → `py-3` (1rem → 0.75rem)
- Removed `linebreaks` filter
- Added `whitespace-pre-wrap` to preserve original formatting
- Preserves line breaks without adding extras

**Testing**:
```python
# In Django shell:
section = Section.objects.first()
print(repr(section.content))  # Check for \n characters
```

### Issue 3: Interactive Terms Not Clickable or Not Showing Icons

**Symptom**:
- Terms appear as regular text, not underlined
- Magnifying glass icon missing
- Clicking doesn't open modal

**Diagnosis Steps**:
1. Check browser console for JavaScript errors
2. Inspect article HTML for `<button class="term-button">`
3. Check API response for `rendered_body` containing `__TERM:`

**Common Causes & Solutions**:

| Problem | Check | Solution |
|---------|-------|----------|
| No `__TERM:` markers in rendered_body | API response | Verify article body has `[[slug]]` format |
| Button styling missing | CSS (style.css) | Ensure term-button class defined |
| Click handler not working | modal.js loaded | Check script tag in base.html |
| Modal doesn't display | browser console | Check fetch endpoint and JSON structure |

**Debug Steps**:
```javascript
// In browser console:
fetch('/api/articles/my-article/')
    .then(r => r.json())
    .then(data => {
        console.log(data.rendered_body);  // Should contain __TERM:
        console.log(data.referenced_terms);  // Should list all terms
    });
```

### Issue 4: Modal Backdrop Click Closes Modal Even for Internal Clicks

**Symptom**:
Clicking a button inside the modal closes the modal instead of activating the button.

**Root Cause**:
Event listener on backdrop catches all clicks, including bubbled events.

**Incorrect Implementation**:
```javascript
// WRONG: Catches all clicks in modal area
modalBackdrop.addEventListener('click', hideModal);
```

**Correct Implementation**:
```javascript
// RIGHT: Only closes on backdrop itself
modalBackdrop.addEventListener('click', (e) => {
    if (e.target === modalBackdrop) {
        hideModal();
    }
});
```

**Why It Matters**:
- Click event bubbles up from button → modal-content → backdrop
- Must check `e.target === modalBackdrop`
- Prevents accidental modal closure

---

## Performance Optimization

### Database Optimization

#### Query Reduction with Prefetch
```python
# BEFORE: N+1 queries problem
articles = Article.objects.all()
for article in articles:
    sections = article.sections.all()  # Extra query per article

# AFTER: Single query for sections
articles = Article.objects.prefetch_related('sections')
for article in articles:
    sections = article.sections.all()  # No additional queries
```

**Impact**: Reduces 11 articles × 3 sections = 33 queries → 2 queries

#### Index Strategy
```python
class MediaInteraction(models.Model):
    # ...
    class Meta:
        indexes = [
            models.Index(fields=['media_item', '-timestamp']),
        ]
```

**Use Case**: Quickly fetch recent interactions for a media item.

#### Exclude Empty Slugs
```python
# BEFORE: Includes articles with empty slugs
articles = Article.objects.filter(is_active=True)

# AFTER: Excludes old data with empty slugs
articles = Article.objects.filter(
    is_active=True,
    slug__isnull=False
).exclude(slug='')
```

### Frontend Optimization

#### Lazy Loading Strategy
- Images/videos load on-demand via modal
- Only fetches media when user interacts
- Reduces initial page load

#### Static Asset Optimization
- Tailwind CSS via CDN for development
- FontAwesome icons as font file (not images)
- Vanilla JavaScript (no framework overhead)

#### CSS Optimization
- Utility classes (Tailwind) vs custom CSS
- Production: Use Tailwind's PurgeCSS to remove unused styles
- Result: ~8KB CSS instead of 50KB+

### Caching Strategy

#### Browser Caching
Configure `settings.py`:
```python
# Cache static files for 30 days
STATIC_ROOT = 'staticfiles/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
```

#### API Response Caching
```python
# In views.py - cache article list for 5 minutes
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)
def article_list(request):
    return render(request, 'index.html')
```

#### Database Connection Pooling
For PostgreSQL production:
```python
# Use pgBouncer or similar connection pooling
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'teaching_platform',
        'CONN_MAX_AGE': 600,  # Persistent connections
    }
}
```

---

## Future Enhancements

### 1. User Authentication & Authorization

**Features**:
- Student registration and login
- Instructor dashboard for content creation
- Role-based permissions
- Student progress tracking

**Implementation**:
```python
# Use Django's built-in auth
from django.contrib.auth.models import User

class StudentProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True)
```

### 2. Advanced Search & Filtering

**Features**:
- Full-text search across article bodies and titles
- Filter by media type, creation date, popularity
- Search result highlighting
- Elasticsearch integration for scalability

**API Endpoint**:
```
GET /api/articles/search/?q=physical+ai&media_type=video
```

### 3. Content Versioning

**Features**:
- Track article edits over time
- Rollback to previous versions
- Diff view between versions
- Author attribution

**Database Addition**:
```python
class ArticleVersion(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    version_number = models.IntegerField()
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

### 4. Multimedia Enhancement

**Features**:
- Image optimization (WebP format, responsive sizes)
- Video transcoding (multiple quality levels)
- Audio transcription and subtitle generation
- Thumbnail generation for videos

**Implementation**:
```python
# Use Celery for async processing
@shared_task
def transcode_video(media_item_id):
    """Convert video to multiple formats in background"""
    item = MediaItem.objects.get(id=media_item_id)
    # Use FFmpeg to create 720p, 480p, 360p versions
```

### 5. Engagement Features

**Features**:
- User comments on articles
- Discussion threads
- Like/favorite articles
- Social media sharing

**Database**:
```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ArticleRating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '⭐'), (5, '⭐⭐⭐⭐⭐')])
```

### 6. Analytics Dashboard

**Features**:
- Engagement metrics (views, interactions)
- User learning paths
- Content performance reports
- Heat maps of clicked terms

**Implementation**:
```python
# Aggregate interactions for dashboard
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

last_7_days = timezone.now() - timedelta(days=7)
popular_media = MediaItem.objects.annotate(
    click_count=Count('interactions')
).filter(
    interactions__timestamp__gte=last_7_days
).order_by('-click_count')[:5]
```

---

## Development Workflow

### Creating a New Article via Admin

1. Navigate to http://localhost:8000/admin/
2. Click "Articles" in the Content section
3. Click "Add Article" button
4. Fill fields:
   - **Title**: Auto-generates slug (or manually enter)
   - **Subtitle**: Optional description
   - **Body**: Use `[[term_slug]]` for interactive terms
   - **Is Active**: Check to publish
5. Scroll to "Add section" and create 3-5 sections
6. Click "Save"

### Creating Article via Management Command

```python
# Create multimedia
media = MediaItem.objects.create(
    title="Example Video",
    media_type="video",
    description="Demo video",
    file=request.FILES['video']
)

# Create article with term markers
article = Article.objects.create(
    title="My Article",
    body="Learn about [[key-concept]] here"
)

# Create term linking to media
term = Term.objects.create(
    slug="key-concept",
    label="Key Concept",
    media_item=media
)

# Create sections
Section.objects.create(
    article=article,
    section_type='introduction',
    title="Getting Started",
    content="Introductory content...",
    order=0
)
```

### Testing Workflow

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.content

# Run with verbosity for detailed output
python manage.py test apps.content -v 2

# Test with coverage (install coverage package)
coverage run --source='.' manage.py test
coverage report
```

### Deployment Checklist

**Security**:
- [ ] Set `DEBUG = False` in settings.py
- [ ] Configure `ALLOWED_HOSTS` for production domain
- [ ] Use environment variables for SECRET_KEY
- [ ] Enable HTTPS/SSL certificates
- [ ] Set secure cookie flags

**Database**:
- [ ] Switch to PostgreSQL (not SQLite)
- [ ] Configure database backups
- [ ] Run migrations in production
- [ ] Create superuser account

**Static Files**:
- [ ] Run `python manage.py collectstatic`
- [ ] Use WhiteNoise for serving static files
- [ ] Or configure CDN for static assets

**Monitoring**:
- [ ] Set up error tracking (Sentry)
- [ ] Configure logging
- [ ] Monitor database performance
- [ ] Track API response times

### Production Configuration Example

```python
# settings.py for production
DEBUG = False
ALLOWED_HOSTS = ['teaching-platform.com', 'www.teaching-platform.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': '5432',
        'CONN_MAX_AGE': 600,
    }
}

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

---

## Code Quality & Architecture

This project demonstrates several software engineering best practices:

### Clean Code Principles

**Separation of Concerns**:
- Models: Data and validation logic
- Views/ViewSets: Request handling
- Serializers: Data transformation
- Templates: Presentation logic

**DRY (Don't Repeat Yourself)**:
- Base template inheritance
- Serializer method fields for computed values
- Reusable admin fieldsets

**Meaningful Names**:
- `rendered_body` vs `body` clearly distinguished
- `referenced_terms` for computed list
- `interaction_count` for aggregated data

### RESTful API Design

- **Proper HTTP Methods**: GET for retrieval, POST for creation
- **Status Codes**: 200 (OK), 201 (Created), 404 (Not Found), 400 (Bad Request)
- **Pagination**: Prevents large data transfers
- **Filtering**: Query parameters for flexibility

### Security by Design

- **CSRF Tokens**: Automatic via Django middleware
- **SQL Injection Prevention**: ORM parameterizes all queries
- **XSS Prevention**: Template auto-escaping enabled
- **Read-Only Fields**: Sensitive data marked as read-only in forms

### Maintainability

- **Type Hints**: Can be added to functions and class methods
- **Docstrings**: Document complex methods
- **Comments**: Explain "why", not "what"
- **Configuration**: Settings externalized from code

# Interactive Teaching Platform

Professional-grade Django-based interactive learning platform with REST API, multimedia content delivery, and comprehensive educator tools. This project demonstrates modern web development practices including responsive design, API-first architecture, and analytics integration.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture Overview](#architecture-overview)
3. [Database Design](#database-design)
4. [Installation & Setup](#installation--setup)
5. [REST API Documentation](#rest-api-documentation)
6. [Frontend Architecture](#frontend-architecture)
7. [Code Patterns & Design Decisions](#code-patterns--design-decisions)
8. [Performance Optimizations](#performance-optimizations)
9. [Security Features](#security-features)
10. [Admin Interface Features](#admin-interface-features)
11. [Production Deployment](#production-deployment)
12. [Testing & Validation](#testing--validation)
13. [Key Design Principles](#key-design-principles)
14. [Troubleshooting](#troubleshooting)
15. [Project Structure](#project-structure)
16. [Feature Roadmap](#feature-roadmap)
17. [Additional Resources](#additional-resources)

---

## Project Overview

### Purpose

The Interactive Teaching Platform is a Django-based web application designed to facilitate interactive learning experiences. It provides educators with powerful tools to create engaging multimedia lessons while offering learners an intuitive interface for exploring educational content.

### Key Features

✨ **Multimedia Content Support:**
- Rich text content with markdown support
- Embedded images with responsive sizing
- Audio playback with custom controls
- Video integration (HTML5 and YouTube)
- Responsive design with Tailwind CSS

🎯 **Interactive Learning Features:**
- Clickable highlighted terms with inline definitions
- Expandable accordion sections for progressive disclosure
- Real-time analytics tracking for engagement metrics
- Section progress tracking
- User interaction logging

👨‍🎓 **Educator Tools:**
- Comprehensive Django admin interface
- Bulk content management
- Media library organization
- Section and term management
- Analytics dashboard

### Technology Stack

| Layer | Technology |
|-------|-----------|
| **Backend Framework** | Django 4.x |
| **REST API** | Django REST Framework |
| **Frontend UI Framework** | Tailwind CSS 3.x |
| **JavaScript Runtime** | Vanilla JavaScript (no frameworks) |
| **Database** | SQLite (development), PostgreSQL (production) |
| **Templating** | Django Templates with Jinja2 |
| **Authentication** | Django built-in authentication |
| **CORS Handling** | django-cors-headers |
| **API Documentation** | Built-in DRF API Browser |

---

## Architecture Overview

### System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Browser                         │
│              (HTML + CSS + JavaScript)                  │
└──────────────────────┬──────────────────────────────────┘
                       │ HTTP/AJAX
┌──────────────────────▼──────────────────────────────────┐
│              Django Application Layer                    │
├─────────────────────────────────────────────────────────┤
│  - URL Routing (urls.py)                               │
│  - View Functions/Classes (views.py)                   │
│  - Template Rendering (templates/)                     │
│  - Static File Handling (CSS, JavaScript)              │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│           REST API Layer (DRF)                          │
├─────────────────────────────────────────────────────────┤
│  - Serializers (data transformation)                   │
│  - ViewSets (CRUD operations)                          │
│  - URL Routing (/api/ endpoints)                       │
│  - Authentication & Permissions                         │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│            Business Logic Layer                         │
├─────────────────────────────────────────────────────────┤
│  - Models (Article, Section, Term, MediaItem)          │
│  - Model Methods & Properties                          │
│  - Signal Handlers                                     │
│  - Custom Managers                                     │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│           Database Layer (ORM)                          │
├─────────────────────────────────────────────────────────┤
│  - SQLite (Development)                                │
│  - PostgreSQL (Production)                             │
│  - Migrations & Schema Management                      │
└─────────────────────────────────────────────────────────┘
```

### Core Components

**Django Views**: Handle HTTP requests and render templates
**Serializers**: Transform model instances to/from JSON
**Models**: Define data structure and business rules
**Templates**: Present formatted HTML to users
**Static Assets**: CSS and JavaScript for frontend interactivity
**Admin Interface**: Content management and analytics

---

## Database Design

### Entity Relationship Diagram

```
┌─────────────────┐        ┌──────────────────┐
│    Article      │────┐   │     Section      │
├─────────────────┤    │   ├──────────────────┤
│ id (PK)         │    └──→│ id (PK)          │
│ title           │        │ article_id (FK)  │
│ slug            │        │ title            │
│ description     │        │ order            │
│ created_at      │        │ accordion_title  │
│ updated_at      │        └──────────────────┘
└─────────────────┘                │
                                   │ 1:N
                        ┌──────────▼──────────┐
                        │    MediaItem        │
                        ├─────────────────────┤
                        │ id (PK)             │
                        │ section_id (FK)     │
                        │ type (video, etc)   │
                        │ content             │
                        │ order               │
                        └─────────────────────┘

┌─────────────────┐
│      Term       │
├─────────────────┤
│ id (PK)         │
│ word            │
│ definition      │
│ article_id (FK) │
│ created_at      │
│ updated_at      │
└─────────────────┘

┌──────────────────────┐
│   UserInteraction    │
├──────────────────────┤
│ id (PK)              │
│ user_id (FK)         │
│ term_id (FK)         │
│ interaction_type     │
│ timestamp            │
└──────────────────────┘
```

### Core Models

#### Article
- **Purpose**: Represents a complete educational lesson or module
- **Key Fields**: title, slug, description, created_at, updated_at
- **Relationships**: One-to-many with Section and Term
- **Key Methods**: get_absolute_url(), get_terms(), get_section_count()

#### Section
- **Purpose**: Represents expandable accordion sections within an article
- **Key Fields**: article (FK), title, order, accordion_title, content_type
- **Relationships**: One-to-many with MediaItem, many-to-one with Article
- **Key Methods**: get_media_items(), display_order()

#### MediaItem
- **Purpose**: Stores different types of multimedia content
- **Types**: TEXT, IMAGE, AUDIO, VIDEO, YOUTUBE
- **Key Fields**: section (FK), type, content, order, metadata (JSON)
- **Key Methods**: get_display_content(), render_html()

#### Term
- **Purpose**: Represents clickable definitions within articles
- **Key Fields**: word, definition, article (FK)
- **Relationships**: One-to-many with UserInteraction
- **Key Methods**: get_interaction_count(), get_recent_interactions()

#### UserInteraction
- **Purpose**: Tracks user engagement with terms
- **Key Fields**: user (FK), term (FK), interaction_type, timestamp
- **Query Optimization**: Indexed on (user_id, timestamp) and (term_id)

---

## Installation & Setup

### Prerequisites

- Python 3.9+
- pip (Python package manager)
- Git
- Virtual environment tool (venv)
- SQLite3 (included with Python)

### Step-by-Step Installation

#### 1. Clone and Navigate
```bash
git clone <repository-url>
cd "g:\Job test\Interactive Teaching Platform"
```

#### 2. Create Virtual Environment
```bash
python -m venv venv
```

#### 3. Activate Virtual Environment

**Windows (PowerShell):**
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
& ".\venv\Scripts\Activate.ps1"
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

#### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 5. Create Environment File
```bash
# Create a .env file in the project root with:
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
DJANGO_SETTINGS_MODULE=config.settings
```

#### 6. Run Database Migrations
```bash
python manage.py migrate --noinput
```

#### 7. Create Superuser
```bash
python manage.py createsuperuser
# or use the automated script:
python manage.py shell < create_superuser.py
```

#### 8. Load Sample Data
```bash
python manage.py load_sample_data
```

#### 9. Collect Static Files (Production)
```bash
python manage.py collectstatic --noinput
```

#### 10. Start Development Server
```bash
# Basic server (with threading and auto-reload)
python manage.py runserver

# or for specific configuration:
python manage.py runserver 0.0.0.0:8000
```

The application will be available at `http://localhost:8000/`

Admin interface: `http://localhost:8000/admin/`

### Verification Checklist

- [ ] Virtual environment activated
- [ ] All dependencies installed (pip freeze shows all packages)
- [ ] Database migrated successfully
- [ ] Superuser created
- [ ] Sample data loaded
- [ ] Development server running without errors
- [ ] Homepage accessible at http://localhost:8000/
- [ ] Admin interface at http://localhost:8000/admin/
- [ ] API endpoints accessible at http://localhost:8000/api/

---

## REST API Documentation

### API Overview

The platform provides a comprehensive REST API built with Django REST Framework. All endpoints return JSON responses and support standard HTTP methods.

### Base URL
```
http://localhost:8000/api/
```

### Authentication

Currently, the API allows anonymous access with optional user authentication for tracking interactions.

### CORS Configuration

```python
# config/settings.py
INSTALLED_APPS = [
    'corsheaders',
    ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "https://example.com",  # Production domain
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
```

### Endpoint 1: List Articles

**Request:**
```http
GET /api/articles/
```

**Response (200 OK):**
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Introduction to Biology",
      "slug": "introduction-to-biology",
      "description": "Learn the fundamentals of biology",
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-20T14:45:00Z",
      "section_count": 3,
      "term_count": 12
    }
  ]
}
```

**Query Parameters:**
- `search`: Search articles by title or description
- `page`: Pagination (default: 1, size: 20)
- `ordering`: Sort by field (e.g., `-created_at`)

**Example:**
```
GET /api/articles/?search=biology&ordering=-created_at
```

### Endpoint 2: Retrieve Article Detail

**Request:**
```http
GET /api/articles/{id}/
```

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "Introduction to Biology",
  "slug": "introduction-to-biology",
  "description": "Learn the fundamentals...",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-20T14:45:00Z",
  "sections": [
    {
      "id": 1,
      "title": "Basic Concepts",
      "order": 1,
      "accordion_title": "Understanding Life",
      "media_items": [
        {
          "id": 1,
          "type": "text",
          "content": "Biology is the study...",
          "order": 1
        },
        {
          "id": 2,
          "type": "image",
          "content": "http://example.com/image.jpg",
          "order": 2
        }
      ]
    }
  ],
  "terms": [
    {
      "id": 1,
      "word": "Organism",
      "definition": "A living individual..."
    }
  ]
}
```

**Error Response (404 Not Found):**
```json
{
  "detail": "Not found."
}
```

### Endpoint 3: List Sections

**Request:**
```http
GET /api/sections/?article={article_id}
```

**Response (200 OK):**
```json
{
  "count": 3,
  "results": [
    {
      "id": 1,
      "article": 1,
      "title": "Introduction",
      "order": 1,
      "accordion_title": "Foundations",
      "media_count": 4
    }
  ]
}
```

### Endpoint 4: List Media Items

**Request:**
```http
GET /api/media/?section={section_id}
```

**Response (200 OK):**
```json
{
  "count": 4,
  "results": [
    {
      "id": 1,
      "section": 1,
      "type": "text",
      "content": "Rich content...",
      "order": 1,
      "metadata": {"format": "markdown"}
    },
    {
      "id": 2,
      "section": 1,
      "type": "youtube",
      "content": "dQw4w9WgXcQ",
      "order": 2,
      "metadata": {"width": 560, "height": 315}
    }
  ]
}
```

**Supported Media Types:**
- `text`: Plain or markdown-formatted text
- `image`: Image URL with responsive sizing
- `audio`: Audio file URL with HTML5 player
- `video`: HTML5 video file URL
- `youtube`: YouTube video ID

### Endpoint 5: List Terms

**Request:**
```http
GET /api/terms/?article={article_id}
```

**Response (200 OK):**
```json
{
  "count": 12,
  "results": [
    {
      "id": 1,
      "word": "Photosynthesis",
      "definition": "Process by which plants convert...",
      "article": 1,
      "created_at": "2024-01-15T10:30:00Z"
    }
  ]
}
```

**Query Parameters:**
- `search`: Search terms by word
- `article`: Filter by article ID

### Endpoint 6: User Interactions (Track Term Views)

**Request:**
```http
POST /api/interactions/
Content-Type: application/json

{
  "term_id": 1,
  "interaction_type": "view"
}
```

**Response (201 Created):**
```json
{
  "id": 42,
  "user": null,
  "term": 1,
  "interaction_type": "view",
  "timestamp": "2024-01-20T14:45:23.456789Z"
}
```

**Supported Interaction Types:**
- `view`: User clicked/viewed a term
- `hover`: User hovered over a term
- `share`: User shared a term

### Endpoint 7: Analytics Summary

**Request:**
```http
GET /api/analytics/summary/?article={article_id}
```

**Response (200 OK):**
```json
{
  "article_id": 1,
  "article_title": "Introduction to Biology",
  "total_views": 345,
  "total_interactions": 892,
  "top_terms": [
    {
      "id": 5,
      "word": "Organism",
      "interaction_count": 127
    }
  ],
  "engagement_by_section": [
    {
      "section_id": 1,
      "section_title": "Foundations",
      "interaction_count": 234
    }
  ]
}
```

### Common Response Codes

| Code | Description |
|------|-------------|
| 200 | Request successful |
| 201 | Resource created successfully |
| 204 | No content (successful deletion) |
| 400 | Bad request (invalid parameters) |
| 401 | Unauthorized (authentication required) |
| 403 | Forbidden (permission denied) |
| 404 | Resource not found |
| 500 | Server error |

### Rate Limiting

Currently not enforced. For production, consider adding:
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
    }
}
```

---

## Frontend Architecture

### Template Hierarchy

```
templates/
├── base.html                 (Master template with header/footer)
├── home.html                 (Homepage - lists all articles)
├── article_detail.html       (Individual article with full content)
├── 404.html                  (Custom 404 error page)
├── 500.html                  (Custom 500 error page)
└── components/
    ├── header.html           (Navigation and branding)
    ├── footer.html           (Footer content)
    ├── hero.html             (Hero section with purple gradient)
    └── breadcrumbs.html      (Navigation breadcrumbs)
```

### Component System

#### 1. Hero Component
- **Purpose**: Display prominent article title and description
- **Styling**: Purple gradient background, responsive padding
- **Usage**: At the top of article_detail.html
- **Customization**: Background color, text alignment

#### 2. Accordion Component
- **Purpose**: Expandable section management
- **Features**: Click-to-expand, smooth animations, state persistence
- **JavaScript**: vanilla-accordion.js
- **CSS Classes**: `.accordion`, `.accordion-item`, `.accordion-content`

#### 3. Term Definition Modal
- **Purpose**: Display term definitions on click
- **Trigger**: Clicking highlighted terms (marked with `<span class="term">`)
- **JavaScript**: term-modal.js
- **Features**: Smooth fade-in, click-outside to close, keyboard navigation

#### 4. Media Renderer
- **Purpose**: Render different media types
- **Types**: Text, Image, Audio, Video, YouTube
- **JavaScript**: media-renderer.js
- **Features**: Responsive sizing, lazy loading, error handling

#### 5. Analytics Tracker
- **Purpose**: Log user interactions
- **Events**: Term views, section opens, media plays
- **Endpoint**: `/api/interactions/`
- **Debouncing**: Prevent excessive API calls

### CSS Architecture (Tailwind CSS)

**Structure:**
- Utility-first approach using Tailwind CSS 3.x
- Custom color palette with purple as primary
- Responsive breakpoints: mobile, tablet, desktop
- Dark mode support (optional)

**Key Tailwind Classes Used:**
```tailwind
/* Layout */
container, flex, grid, gap, p-*, m-*

/* Typography */
text-*, font-*, leading-*, tracking-*

/* Colors */
bg-purple-*, text-purple-*, border-purple-*

/* Responsive */
md:*, lg:*, xl:*, 2xl:*

/* Interactivity */
hover:*, focus:*, active:*, disabled:*

/* States */
dark:*, group-hover:*
```

**Custom Tailwind Configuration:**
```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'primary': '#8b5cf6',  // Purple
        'secondary': '#6366f1', // Indigo
      },
      animation: {
        fadeIn: 'fadeIn 0.3s ease-in-out',
      },
    },
  },
  plugins: [],
}
```

### JavaScript Patterns

#### 1. Module Pattern
```javascript
// Example: term-modal.js
const TermModal = (() => {
  const init = () => {
    setupEventListeners();
  };
  
  const setupEventListeners = () => {
    document.querySelectorAll('.term').forEach(el => {
      el.addEventListener('click', showTermDefinition);
    });
  };
  
  const showTermDefinition = (e) => {
    // Implementation
  };
  
  return { init };
})();

document.addEventListener('DOMContentLoaded', TermModal.init);
```

#### 2. Event Delegation
```javascript
// Single event listener on parent
document.addEventListener('click', (e) => {
  if (e.target.matches('.accordion-trigger')) {
    toggleAccordion(e.target);
  }
});
```

#### 3. Fetch API for AJAX
```javascript
// Post interaction data
fetch('/api/interactions/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': getCookie('csrftoken'),
  },
  body: JSON.stringify({
    term_id: 1,
    interaction_type: 'view'
  })
})
.then(response => response.json())
.then(data => console.log('Success:', data))
.catch(error => console.error('Error:', error));
```

#### 4. Debouncing
```javascript
const debounce = (func, delay) => {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func(...args), delay);
  };
};

// Usage: Debounce analytics tracking
const trackTermView = debounce((termId) => {
  recordInteraction(termId, 'view');
}, 300);
```

### Responsive Design

**Mobile-First Approach:**
- Single column layout on mobile
- 2-column layout on tablets
- 3-column layout on desktop (if needed)
- Hamburger menu for navigation
- Touch-friendly button sizes (minimum 44px)

**Breakpoints:**
```tailwind
sm: 640px   // Tablets
md: 768px   // Small laptops
lg: 1024px  // Desktop
xl: 1280px  // Large desktop
2xl: 1536px // Ultra-wide
```

**Media Query Example:**
```css
/* Mobile First */
.article-grid {
  @apply grid grid-cols-1 gap-4;
}

@media (min-width: 768px) {
  .article-grid {
    @apply grid-cols-2;
  }
}
```

---

## Code Patterns & Design Decisions

### Pattern 1: Model Property Methods for Computed Values

**Problem:** Avoid recalculating complex values in templates

**Solution:** Use `@property` decorators on models

```python
# models.py
class Article(models.Model):
    title = models.CharField(max_length=200)
    
    @property
    def section_count(self):
        """Get total number of sections"""
        return self.sections.count()
    
    @property
    def average_engagement(self):
        """Calculate average engagement score"""
        from django.db.models import Avg
        return self.sections.annotate(
            avg_views=Avg('media_items__interactions')
        ).aggregate(Avg('avg_views'))['avg_views__avg']
    
    # Template usage: {{ article.section_count }}
```

### Pattern 2: QuerySet Methods for Reusable Filters

**Problem:** DRY principle for complex database queries

**Solution:** Use custom managers and QuerySet methods

```python
# models.py
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)

class Article(models.Model):
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    
    objects = PublishedManager()
    
    # Usage: Article.objects.all() returns only published articles
```

### Pattern 3: Serializer Method Fields for API Responses

**Problem:** Include related data or computed values in API responses

**Solution:** Use `SerializerMethodField` in DRF serializers

```python
# serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    section_count = serializers.SerializerMethodField()
    terms = TermSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'section_count', 'terms']
    
    def get_section_count(self, obj):
        """Count sections for this article"""
        return obj.sections.count()
```

### Pattern 4: Signals for Automatic Updates

**Problem:** Keep denormalized data in sync automatically

**Solution:** Use Django signals for post-save hooks

```python
# models.py or signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=MediaItem)
def update_section_media_count(sender, instance, created, **kwargs):
    """Update parent section's media count after item is saved"""
    if instance.section:
        instance.section.update_media_count()

@receiver(post_delete, sender=MediaItem)
def update_section_on_delete(sender, instance, **kwargs):
    """Update parent section when media item is deleted"""
    if instance.section:
        instance.section.update_media_count()
```

### Pattern 5: Context Processors for Global Template Data

**Problem:** Avoid passing same data to every view

**Solution:** Use context processors to inject global context

```python
# context_processors.py
def site_config(request):
    return {
        'site_name': 'Interactive Teaching Platform',
        'current_year': timezone.now().year,
        'support_email': 'support@example.com',
    }

# settings.py
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'OPTIONS': {
        'context_processors': [
            'myapp.context_processors.site_config',
        ],
    },
}]

# Template: {{ site_name }} is automatically available
```

### Pattern 6: ViewSet Actions for Custom Endpoints

**Problem:** Need custom endpoints beyond standard CRUD

**Solution:** Use `@action` decorator on ViewSets

```python
# views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    @action(detail=True, methods=['get'])
    def analytics(self, request, pk=None):
        """Get analytics for a specific article"""
        article = self.get_object()
        analytics_data = {
            'total_views': article.get_total_views(),
            'engagement_rate': article.get_engagement_rate(),
            'top_terms': article.get_top_terms(limit=5),
        }
        return Response(analytics_data)
    
    # Usage: GET /api/articles/1/analytics/
```

### Pattern 7: Pagination for Large Result Sets

**Problem:** API returns too much data, slow response times

**Solution:** Implement pagination in serializers

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

# views.py - Pagination automatic with these settings
# Usage: GET /api/articles/?page=1
```

### Pattern 8: Lazy Loading for Performance

**Problem:** Load related objects only when needed

**Solution:** Use `select_related()` and `prefetch_related()`

```python
# views.py
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    
    def get_queryset(self):
        # Reduce database queries with select_related for FK
        # and prefetch_related for M2M or reverse FK
        return Article.objects.select_related(
            'author'
        ).prefetch_related(
            'sections',
            'sections__media_items',
            'terms'
        )
```

---

## Performance Optimizations

### Database Query Optimization

#### 1. Query Reduction with select_related()
```python
# Bad: N+1 query problem
for article in Article.objects.all():
    print(article.author.name)  # Hits database N times

# Good: Fetch related data in single query
for article in Article.objects.select_related('author'):
    print(article.author.name)  # Single query
```

#### 2. Batch Processing with prefetch_related()
```python
# Bad: Separate query per article
for article in Article.objects.all():
    for section in article.sections.all():
        print(section.title)

# Good: Two queries total
articles = Article.objects.prefetch_related('sections')
for article in articles:
    for section in article.sections.all():
        print(section.title)
```

#### 3. Using `only()` and `defer()` for Column Selection
```python
# Only select needed columns
articles = Article.objects.only('id', 'title', 'slug')

# Exclude heavy columns
articles = Article.objects.defer('description', 'content')
```

#### 4. Query Counting in Development
```python
# Development settings
if DEBUG:
    from django.db import connection
    from django.db.backends.utils import CursorDebugWrapper
    
    CursorDebugWrapper.enable()
    
    # Later check:
    print(len(connection.queries))  # Number of queries executed
```

#### 5. Database Indexing Strategy
```python
# models.py
class Article(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True)  # Unique implies index
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['created_at', 'title']),  # Composite index
            models.Index(fields=['-created_at']),  # Reverse ordering
        ]
```

### Frontend Performance

#### 1. Lazy Loading Images
```html
<!-- Standard (loads immediately) -->
<img src="image.jpg" alt="Description">

<!-- Lazy loaded (loads on scroll) -->
<img loading="lazy" src="image.jpg" alt="Description">
```

#### 2. JavaScript Code Splitting
```javascript
// Load only when needed
const loadTermModal = () => {
    import('./term-modal.js').then(module => {
        module.TermModal.init();
    });
};

document.addEventListener('DOMContentLoaded', loadTermModal);
```

#### 3. CSS Minification and Tree-Shaking
```bash
# Development
npm run tailwind:dev

# Production (removes unused styles)
npm run tailwind:build
```

#### 4. Static Asset Compression
```python
# settings.py (Production)
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Serves .gz compressed versions
MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
]
```

### Caching Strategy

#### 1. Cache Template Fragments
```django
{% load cache %}
{% cache 3600 article_section article.id section.id %}
    <div class="section">
        {% include 'components/section.html' %}
    </div>
{% endcache %}
```

#### 2. Cache API Responses
```python
# views.py
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)  # 5 minutes
def get_popular_articles(request):
    return Response(popular_articles_data())
```

#### 3. Use Django's Low-Level Cache
```python
# views.py
from django.core.cache import cache

def get_article_analytics(request, pk):
    cache_key = f'analytics_article_{pk}'
    data = cache.get(cache_key)
    
    if data is None:
        data = calculate_analytics(pk)
        cache.set(cache_key, data, 3600)  # Cache 1 hour
    
    return Response(data)
```

#### 4. Cache Configuration
```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

---

## Security Features

### 1. CSRF Protection

**Implementation:**
```django
<!-- All forms include CSRF token -->
<form method="post" action="/api/articles/">
    {% csrf_token %}
    <input type="text" name="title">
    <button type="submit">Save</button>
</form>
```

**Settings:**
```python
# settings.py
CSRF_COOKIE_SECURE = True      # Only send over HTTPS
CSRF_COOKIE_HTTPONLY = False   # Accessible to JavaScript (needed for AJAX)
CSRF_TRUSTED_ORIGINS = [
    'https://example.com',
]
```

**JavaScript AJAX:**
```javascript
const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie) {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const [key, value] = cookie.trim().split('=');
            if (key === name) cookieValue = decodeURIComponent(value);
        }
    }
    return cookieValue;
};

fetch('/api/interactions/', {
    method: 'POST',
    headers: {
        'X-CSRFToken': getCookie('csrftoken'),
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
});
```

### 2. CORS Configuration

**Allowed Origins:**
```python
# settings.py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "https://yourdomain.com",
]

CORS_ALLOW_CREDENTIALS = True
```

**Browser Behavior:** Requests from unapproved origins are blocked

### 3. SQL Injection Prevention

**Django ORM (Safe):**
```python
# ✅ Safe - uses parameterized queries
articles = Article.objects.filter(title=user_input)
article = Article.objects.raw(
    'SELECT * FROM app_article WHERE title = %s',
    [user_input]  # Parameters are separate
)

# ❌ Dangerous - never do this
articles = Article.objects.raw(
    f'SELECT * FROM app_article WHERE title = {user_input}'
)
```

### 4. Cross-Site Scripting (XSS) Prevention

**Template Auto-Escaping:**
```django
<!-- Django auto-escapes by default -->
<h1>{{ article.title }}</h1>

<!-- If title contains <script>alert('XSS')</script> -->
<!-- Rendered as: &lt;script&gt;alert('XSS')&lt;/script&gt; -->

<!-- Mark content as safe only when trusted -->
{{ article.description|safe }}  <!-- ⚠️ Use carefully -->
```

**Content Security Policy (CSP):**
```python
# settings.py or middleware
def add_csp_header(request):
    response = render(request, 'template.html')
    response['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline'; "
        "style-src 'self' 'unsafe-inline'; "
        "img-src 'self' data: https:; "
    )
    return response
```

### 5. Security Headers

```python
# middleware.py
class SecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        # Prevent MIME type sniffing
        response['X-Content-Type-Options'] = 'nosniff'
        
        # Enable browser XSS filtering
        response['X-XSS-Protection'] = '1; mode=block'
        
        # Prevent clickjacking
        response['X-Frame-Options'] = 'SAMEORIGIN'
        
        # HSTS for HTTPS
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        
        return response
```

### 6. Authentication & Permissions

```python
# views.py
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAuthenticated(), IsAdminUser()]
```

---

## Admin Interface Features

### Article Management

**Location:** `/admin/articles/article/`

**Key Fields:**
- Title (text input)
- Slug (auto-generated)
- Description (textarea)
- Published status (checkbox)
- Created/Updated timestamps

**Actions:**
- Create new article
- Edit existing articles
- Delete articles
- Search by title/slug
- Filter by publication date

**Custom Admin Display:**
```python
# admin.py
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'section_count', 'created_at', 'published']
    list_filter = ['published', 'created_at']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    
    def section_count(self, obj):
        return obj.sections.count()
    section_count.short_description = 'Sections'
```

### Media Item Management

**Location:** `/admin/articles/mediaitem/`

**Supported Types:**
- **TEXT**: Markdown or plain text
- **IMAGE**: Image URL with optional metadata
- **AUDIO**: Audio file URL
- **VIDEO**: HTML5 video URL
- **YOUTUBE**: YouTube video ID

**Inline Management:**
```python
# admin.py
class MediaItemInline(admin.TabularInline):
    model = MediaItem
    extra = 1
    fields = ['type', 'content', 'order']
    ordering = ['order']

class SectionAdmin(admin.ModelAdmin):
    inlines = [MediaItemInline]
```

### Section Management

**Features:**
- Drag-to-reorder functionality
- Accordion title customization
- Associated media items display
- Content preview

### Term Management

**Features:**
- Word input with auto-formatting
- Rich definition field
- Article assignment
- Interaction tracking

---

## Production Deployment

### Environment Variables

Create `.env` file with production settings:

```bash
# Application
DEBUG=False
SECRET_KEY=your-very-secure-random-key-here
ALLOWED_HOSTS=example.com,www.example.com

# Database
DATABASE_URL=postgresql://user:password@host:5432/dbname
DATABASES_NAME=interactive_teaching_platform

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
CSRF_COOKIE_HTTPONLY=True

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Cache
REDIS_URL=redis://:password@127.0.0.1:6379/1

# CDN
AWS_STORAGE_BUCKET_NAME=your-bucket
AWS_S3_REGION_NAME=us-east-1
```

### Database Migration (PostgreSQL)

```bash
# Backup SQLite database
sqlite3 db.sqlite3 ".dump" > backup.sql

# Create PostgreSQL connection
export DATABASE_URL=postgresql://user:password@localhost:5432/teaching_platform

# Run migrations
python manage.py migrate

# Load data if needed
python manage.py load_sample_data
```

### Static Files Collection

```bash
# Collect all static files to single directory
python manage.py collectstatic --noinput --clear

# With CDN/S3:
python manage.py collectstatic --noinput --storage storages.backends.s3boto3.S3Boto3Storage
```

---

---

## Debugging & Troubleshooting

For detailed debugging information, issue analysis, and troubleshooting procedures, please refer to the separate [debugLog.md](./debugLog.md) file. This document includes:

- **Issue 1: Articles Not Displaying** - Complete debugging process and solution
- **Issue 2: Multimedia Content Not Displaying** - Root cause analysis and fixes
- **Issue 3: YouTube URL Validation Errors** - Developer debugging steps
- **Issue 4: YouTube Video Player Errors** - Video ID extraction and embedding solutions
- **Additional Debugging Tips** - Browser console, Django shell, and logging configuration

[📖 Open Debugging Guide](./debugLog.md)

---

## Production Deployment

### Web Server Configuration (Nginx)

```nginx
upstream django {
    server unix:/tmp/gunicorn.sock;
}

server {
    listen 443 ssl http2;
    server_name example.com www.example.com;
    
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    
    client_max_body_size 20M;
    
    location /static/ {
        alias /var/www/teaching-platform/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
    
    location /media/ {
        alias /var/www/teaching-platform/media/;
        expires 7d;
    }
    
    location / {
        proxy_pass http://django;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # Redirect HTTP to HTTPS
    if ($scheme != "https") {
        return 301 https://$server_name$request_uri;
    }
}
```

### Gunicorn Configuration

```bash
# gunicorn.conf.py
bind = "unix:/tmp/gunicorn.sock"
workers = 4
worker_class = "sync"
max_requests = 1000
timeout = 60
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "info"
```

### Systemd Service

```ini
# /etc/systemd/system/gunicorn.service
[Unit]
Description=Gunicorn service for Teaching Platform
After=network.target

[Service]
Type=notify
User=www-data
WorkingDirectory=/var/www/teaching-platform
ExecStart=/var/www/teaching-platform/venv/bin/gunicorn config.wsgi:application
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### Health Checks

```python
# urls.py - Add health check endpoint
from django.http import JsonResponse

def health_check(request):
    try:
        from django.db import connection
        connection.ensure_connection()
        return JsonResponse({'status': 'healthy', 'database': 'connected'})
    except Exception as e:
        return JsonResponse(
            {'status': 'unhealthy', 'error': str(e)},
            status=503
        )

# Include in urls.py
urlpatterns = [
    path('health/', health_check, name='health'),
]
```

---

## Testing & Validation

### Manual Testing Checklist

#### Homepage & Navigation
- [ ] Homepage loads without errors
- [ ] All articles display in grid/list layout
- [ ] Search functionality works
- [ ] Article cards show correct information
- [ ] Navigation menu accessible and functional

#### Article View
- [ ] Article page loads with full content
- [ ] Hero section displays properly
- [ ] Purple gradient applies correctly
- [ ] All sections render with correct content
- [ ] Accordion sections expand/collapse smoothly
- [ ] Media items (images, videos) load correctly

#### Interactive Features
- [ ] Clickable terms highlight on hover
- [ ] Term definition modal appears on click
- [ ] Modal closes on click outside or Esc key
- [ ] Audio player controls work
- [ ] YouTube videos embed and play correctly
- [ ] Images load and scale responsively

#### API Testing
- [ ] Test all 7 endpoints with curl or Postman
- [ ] Verify response structures
- [ ] Check error handling (404, 500, etc.)
- [ ] Verify pagination works
- [ ] Confirm CORS headers present
- [ ] Test analytics tracking

#### Responsive Design
- [ ] Mobile layout (375px): single column
- [ ] Tablet layout (768px): adjusted spacing
- [ ] Desktop layout (1024px): full features
- [ ] Touch targets >= 44px on mobile
- [ ] No horizontal scrolling
- [ ] Images scale properly

#### Performance
- [ ] Page load time < 3 seconds
- [ ] API responses < 500ms
- [ ] Images lazy load correctly
- [ ] No console errors
- [ ] Smooth scrolling and animations

### API Testing with cURL

```bash
# List articles
curl -X GET http://localhost:8000/api/articles/

# Get article detail
curl -X GET http://localhost:8000/api/articles/1/

# Search articles
curl -X GET "http://localhost:8000/api/articles/?search=biology"

# Track interaction
curl -X POST http://localhost:8000/api/interactions/ \
  -H "Content-Type: application/json" \
  -d '{"term_id": 1, "interaction_type": "view"}'

# Get analytics
curl -X GET "http://localhost:8000/api/analytics/summary/?article=1"
```

### Automated Testing Example

```python
# tests.py
from django.test import TestCase, Client
from rest_framework.test import APITestCase
from .models import Article, Section, Term

class ArticleAPITestCase(APITestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title="Test Article",
            description="Test Description"
        )
    
    def test_list_articles(self):
        response = self.client.get('/api/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_article_detail(self):
        response = self.client.get(f'/api/articles/{self.article.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Article')
    
    def test_create_interaction(self):
        term = Term.objects.create(
            word="Test Term",
            definition="Test Definition",
            article=self.article
        )
        response = self.client.post('/api/interactions/', {
            'term_id': term.id,
            'interaction_type': 'view'
        })
        self.assertEqual(response.status_code, 201)

# Run tests
# python manage.py test
```

---

## Key Design Principles

### 1. DRY (Don't Repeat Yourself)
- Use template inheritance for common layouts
- Create reusable components and modules
- Leverage Django's ORM for consistent queries
- Share CSS utility classes via Tailwind

**Example:**
```python
# models.py - Define business logic once
class Article(models.Model):
    def get_formatted_title(self):
        return self.title.title()

# Usage in template - Call the method
{{ article.get_formatted_title }}
```

### 2. Separation of Concerns
- Models handle data logic
- Views handle request/response
- Templates handle presentation
- JavaScript handles client-side interactivity
- API endpoints handle data access

### 3. Progressive Enhancement
- Core functionality works without JavaScript
- Accordion sections are readable without JS
- Terms display with fallback definitions
- Forms submit with standard HTTP methods

### 4. Responsive by Default
- Mobile-first CSS approach
- Test on multiple screen sizes
- Use Tailwind's responsive prefixes
- Flexible layouts with flexbox/grid

### 5. Performance First
- Lazy load images
- Optimize database queries
- Minimize HTTP requests
- Cache expensive operations
- Monitor with Django Debug Toolbar

### 6. Security by Default
- Validate all user inputs
- Use ORM to prevent SQL injection
- Enable CSRF protection
- Set secure cookie flags
- Implement CORS carefully

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: "ModuleNotFoundError: No module named 'django'"

**Solution:**
```bash
# Activate virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

#### Issue: "No such table: app_article"

**Solution:**
```bash
# Run migrations
python manage.py migrate

# Or reset database (development only)
rm db.sqlite3
python manage.py migrate
python manage.py load_sample_data
```

#### Issue: Static files not loading in production

**Solution:**
```bash
# Collect static files
python manage.py collectstatic --noinput --clear

# Check STATIC_ROOT in settings
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
```

#### Issue: CSRF token missing

**Solution:**
```django
<!-- In HTML forms -->
{% csrf_token %}

<!-- In AJAX requests -->
<script>
const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie) {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            if (cookie.trim().startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.trim().substring(name.length + 1));
            }
        }
    }
    return cookieValue;
};

fetch('/api/endpoint/', {
    method: 'POST',
    headers: {'X-CSRFToken': getCookie('csrftoken')},
    body: JSON.stringify(data)
});
</script>
```

#### Issue: CORS errors in console

**Solution:**
```python
# settings.py
INSTALLED_APPS = [
    'corsheaders',
    ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
]
```

#### Issue: Images not displaying

**Solution:**
```python
# settings.py - Configure media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# urls.py - Serve media files in development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your patterns
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

#### Issue: Slow database queries

**Solution:**
```python
# views.py - Use select_related and prefetch_related
from django.db.models import Prefetch

class ArticleListView(ListView):
    def get_queryset(self):
        return Article.objects.select_related(
            'author'
        ).prefetch_related(
            'sections__media_items',
            'terms'
        )

# Or use Django Debug Toolbar
# pip install django-debug-toolbar
```

#### Issue: "ALLOWED_HOSTS" error in production

**Solution:**
```python
# settings.py
ALLOWED_HOSTS = [
    'example.com',
    'www.example.com',
    '127.0.0.1',
    'localhost',
]

# Or load from environment
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
```

---

## Project Structure

```
Interactive Teaching Platform/
│
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
├── .env.example                       # Example environment variables
│
├── config/                            # Project configuration
│   ├── __init__.py
│   ├── settings.py                    # Main settings
│   ├── urls.py                        # Root URL configuration
│   ├── wsgi.py                        # WSGI application
│   └── asgi.py                        # ASGI application
│
├── apps/                              # Django applications
│   ├── articles/                      # Main app
│   │   ├── migrations/                # Database migrations
│   │   ├── templates/
│   │   │   ├── articles/
│   │   │   │   ├── home.html          # Homepage
│   │   │   │   └── article_detail.html # Article page
│   │   │   └── base.html              # Base template
│   │   ├── static/
│   │   │   ├── css/
│   │   │   │   └── main.css           # Main stylesheet
│   │   │   └── js/
│   │   │       ├── term-modal.js      # Term definition modal
│   │   │       ├── accordion.js       # Accordion functionality
│   │   │       ├── analytics.js       # User tracking
│   │   │       └── media-renderer.js  # Media display
│   │   ├── admin.py                   # Admin configuration
│   │   ├── models.py                  # Database models
│   │   ├── views.py                   # View functions
│   │   ├── serializers.py             # DRF serializers
│   │   ├── urls.py                    # App URLs
│   │   ├── forms.py                   # Django forms
│   │   ├── managers.py                # Custom queryset managers
│   │   └── tests.py                   # Unit tests
│   │
│   └── api/                           # REST API app
│       ├── views.py                   # API viewsets
│       ├── urls.py                    # API URL routing
│       └── tests.py                   # API tests
│
├── venv/                              # Virtual environment
│   └── (dependencies installed here)
│
└── db.sqlite3                         # Development database
```

---

## Feature Roadmap

### Version 1.0 (Current)

✅ **Core Features:**
- Article creation and management
- Section accordion interface
- Multimedia content support (text, images, audio, video, YouTube)
- Clickable term definitions with modal
- User interaction tracking
- REST API (7 endpoints)
- Admin interface
- Responsive design (Tailwind CSS)
- Authentication system

✅ **API Features:**
- Article listing and detail views
- Section management
- Media item handling
- Term definitions
- Interaction tracking
- Basic analytics

### Version 2.0 (Future)

📋 **Planned Features:**

**User Experience:**
- [ ] User accounts and profiles
- [ ] Learning progress tracking
- [ ] User notes and annotations
- [ ] Bookmarks/favorites
- [ ] Quiz functionality
- [ ] Certificate generation
- [ ] Dark mode support

**Content Management:**
- [ ] WYSIWYG editor for content
- [ ] Batch media upload
- [ ] Content versioning
- [ ] Schedule publishing
- [ ] Draft/publish workflow
- [ ] A/B testing content

**Analytics & Reporting:**
- [ ] Advanced analytics dashboard
- [ ] User engagement metrics
- [ ] Content performance reports
- [ ] Export functionality (CSV, PDF)
- [ ] Real-time analytics
- [ ] Heatmap of interactions

**Collaboration:**
- [ ] Multi-author support
- [ ] Comments system
- [ ] Discussion forums
- [ ] Peer review workflow
- [ ] Real-time collaboration

**Performance:**
- [ ] Caching layer optimization
- [ ] CDN integration
- [ ] Image optimization
- [ ] Database query optimization
- [ ] Load testing

**Security:**
- [ ] Two-factor authentication
- [ ] API key management
- [ ] Rate limiting
- [ ] Penetration testing
- [ ] Security audit

---

## Additional Resources

### Documentation
- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Guide](https://www.django-rest-framework.org/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [MDN Web Docs - JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

### Tools & Libraries
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/) - Development debugging
- [Postman](https://www.postman.com/) - API testing
- [ngrok](https://ngrok.com/) - Expose local server publicly
- [Coverage.py](https://coverage.readthedocs.io/) - Test coverage measurement

### Deployment Resources
- [PythonAnywhere](https://www.pythonanywhere.com/) - Simple hosting
- [Heroku](https://www.heroku.com/) - Platform-as-a-service
- [DigitalOcean](https://www.digitalocean.com/) - VPS hosting
- [AWS](https://aws.amazon.com/) - Cloud platform

### Learning Resources
- [Real Python](https://realpython.com/) - Python tutorials
- [Full Stack Python](https://www.fullstackpython.com/) - Web development guide
- [JavaScript.info](https://javascript.info/) - JavaScript fundamentals

### Community
- [Django Forum](https://forum.djangoproject.com/) - Official community
- [Stack Overflow](https://stackoverflow.com/questions/tagged/django) - Q&A site
- [Reddit r/django](https://www.reddit.com/r/django/) - Community discussions

---

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style
- Follow [PEP 8](https://pep8.org/) for Python
- Use double quotes for strings in Python
- Keep lines under 100 characters
- Use meaningful variable and function names
- Add docstrings to functions and classes

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Support & Questions

For questions or issues:
- Check the Troubleshooting section
- Review existing documentation
- Post on community forums
- Contact support team

---

**Last Updated:** January 2024
**Version:** 1.0.0
**Status:** Production Ready

