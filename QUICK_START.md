# Quick Start Guide

Get the Interactive Teaching Platform running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

## Installation Steps

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- Django 5.0.4
- Django REST Framework 3.15.1
- Pillow for image handling
- All other required packages

### 2️⃣ Apply Database Migrations

```bash
python manage.py migrate
```

Creates database tables for:
- Articles
- Sections
- Media Items
- Terms
- Media Interactions

### 3️⃣ Create Admin User

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

**Or use the default:**
- Username: `admin`
- Password: `admin123`

```bash
python manage.py createsuperuser --username admin --email admin@example.com
```

### 4️⃣ Load Sample Data

```bash
python manage.py load_sample_data
```

Creates sample articles and multimedia content for testing.

### 5️⃣ Start Development Server

```bash
python manage.py runserver
```

Server starts at `http://127.0.0.1:8000`

---

## Access Points

| URL | Purpose |
|-----|---------|
| `http://127.0.0.1:8000/` | Public frontend |
| `http://127.0.0.1:8000/admin/` | Admin dashboard |
| `http://127.0.0.1:8000/api/` | API documentation |

---

## First Steps

### Create Your First Article

1. Visit `http://127.0.0.1:8000/admin/`
2. Login with your credentials
3. Click **Articles** → **Add Article**
4. Fill in the form:
   - **Title**: "My First Article"
   - **Subtitle**: "A test article"
   - **Body**: Add content with highlighted terms using `[[term-slug]]`
   - Check **Is active** to publish

### Create Multimedia Content

1. In Admin, click **Media Items** → **Add Media Item**
2. Choose a type:
   - **Text**: Static content
   - **Image**: Upload an image file
   - **Audio**: Upload an MP3/WAV file
   - **Video**: Upload an MP4 file
   - **YouTube**: Paste a YouTube URL

### Link Terms to Media

1. In Admin, click **Terms** → **Add Term**
2. Fill in:
   - **Label**: The text to highlight (e.g., "machine learning")
   - **Slug**: URL-friendly version (e.g., "machine-learning")
   - **Media Item**: Select the multimedia to display

### Create Accordion Sections

1. When editing an Article, scroll to **Sections**
2. Click **Add another Section**
3. Choose section type and add content:
   - **Introduction**
   - **Detailed Explanation**
   - **Additional Resources**

---

## Example Article

Here's a sample article body:

```
Machine learning is a subset of [[artificial-intelligence|artificial intelligence]] that enables 
computers to learn from data. The process involves [[data-preprocessing|preprocessing data]], 
training [[neural-networks|neural networks]], and evaluating performance.

Key concepts include:
- Supervised vs unsupervised learning
- Training/validation/test splits
- [[hyperparameter-tuning|Hyperparameter tuning]]
- Model evaluation metrics
```

When published:
- Highlighted terms appear in yellow
- Clicking them opens a modal with linked multimedia
- Admin can track how many times each term is clicked

---

## API Usage

### Get All Articles

```bash
curl http://127.0.0.1:8000/api/articles/
```

### Get Article with Details

```bash
curl http://127.0.0.1:8000/api/articles/my-article/
```

Response includes:
- Article content
- Expandable sections
- Linked multimedia items

### Get Specific Media Item

```bash
curl http://127.0.0.1:8000/api/media-items/1/
```

### Track Interaction

```bash
curl -X POST http://127.0.0.1:8000/api/media-items/1/track/
```

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **Escape** | Close modal |
| **Tab** | Navigate between modal elements |
| **Enter** | Interact with focused element |

---

## File Structure

```
Project/
├── manage.py              ← Run commands
├── requirements.txt       ← Python dependencies
├── setup.py              ← Run setup.py for automated setup
│
├── apps/
│   ├── content/          ← Main app with models and API
│   └── core/             ← Frontend views and URLs
│
├── templates/
│   └── core/
│       ├── base.html           ← Master template
│       ├── article_detail.html  ← Article page
│       └── index.html           ← Articles list
│
└── static/
    ├── css/style.css          ← Styling
    └── js/modal.js            ← Modal interaction logic
```

---

## Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Permission Errors
```bash
# On Windows, run Command Prompt as Administrator
# Or use: pip install --user -r requirements.txt
```

### Database Issues
```bash
# Reset everything (development only!)
python manage.py flush --no-input
python manage.py migrate
python manage.py load_sample_data
```

### Templates Not Found
```bash
# Ensure static files are configured
python manage.py collectstatic
```

---

## Next Steps

📖 Read [README.md](README.md) for comprehensive documentation
🛠️ Check [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for database operations
📱 Customize [static/css/style.css](static/css/style.css) for your branding
🔌 Extend the API with new endpoints
🧪 Add tests in [apps/content/tests.py](apps/content/tests.py)

---

## Support

Need help?
1. Check the README.md
2. Review Django documentation: https://docs.djangoproject.com
3. Check DRF docs: https://www.django-rest-framework.org

---

**Happy teaching! 🎓**
