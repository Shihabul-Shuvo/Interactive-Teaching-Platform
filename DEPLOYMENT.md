# Deployment Guide - Interactive Teaching Platform

This guide provides comprehensive instructions for deploying the Interactive Teaching Platform to production environments.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Deployment Options](#deployment-options)
3. [Local/Development Deployment](#localdevelopment-deployment)
4. [Production Deployment Steps](#production-deployment-steps)
5. [Server Configuration](#server-configuration)
6. [Environment Variables](#environment-variables)
7. [Security Checklist](#security-checklist)
8. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before deploying, ensure you have:

- Python 3.11+ installed
- Git installed and configured
- Server/hosting provider account (AWS, DigitalOcean, Heroku, etc.)
- Domain name (optional but recommended)
- SSL certificate (recommended for production)
- PostgreSQL installed (for production; SQLite for development)
- Redis installed (optional, for caching)

---

## Deployment Options

### 1. **Heroku** (Easiest - PaaS)
- Automated deployment from Git
- Managed infrastructure
- Free tier available
- Best for: Rapid prototyping and small-scale deployments

### 2. **PythonAnywhere** (Easy - PaaS)
- Pre-configured Python environment
- Web-based console
- Free tier available
- Best for: Small projects and learning

### 3. **AWS EC2** (Medium Complexity)
- Full control over infrastructure
- Scalable
- Pay per usage
- Best for: Production applications with specific requirements

### 4. **DigitalOcean** (Medium Complexity)
- Virtual Private Server (VPS)
- Simple setup
- Affordable pricing
- Best for: Small to medium production deployments

### 5. **Self-Hosted** (Complex)
- Full control
- Best for: Large-scale deployments or specific requirements

---

## Local/Development Deployment

### Running Locally

```bash
# 1. Clone the repository
git clone <repository-url>
cd "Interactive Teaching Platform"

# 2. Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Load sample data (optional)
python manage.py load_sample_data

# 6. Create superuser for admin
python manage.py createsuperuser

# 7. Run development server
python manage.py runserver

# Access at http://localhost:8000
```

---

## Production Deployment Steps

### Step 1: Prepare the Application

```bash
# 1. Install production dependencies
pip install -r requirements.txt

# 2. Update .env file with production settings
# Create .env file in project root:
DEBUG=False
SECRET_KEY=your-secure-random-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
ENVIRONMENT=production
```

### Step 2: Collect Static Files

```bash
# Collect all static files for serving
python manage.py collectstatic --noinput

# This creates a /staticfiles/ directory with all CSS, JS, images
```

### Step 3: Set Up Database (PostgreSQL)

```bash
# Create PostgreSQL database and user
sudo -u postgres psql

# In PostgreSQL shell:
CREATE DATABASE teaching_platform;
CREATE USER teaching_user WITH PASSWORD 'strong_password';
ALTER ROLE teaching_user SET client_encoding TO 'utf8';
ALTER ROLE teaching_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE teaching_user SET default_transaction_deferrable TO on;
ALTER ROLE teaching_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE teaching_platform TO teaching_user;
\q

# Run migrations
python manage.py migrate
```

### Step 4: Configure Production Settings

Update `config/settings.py`:

```python
# settings.py (Production)

import os
from pathlib import Path

# Security Settings
DEBUG = os.getenv('DEBUG', 'False') == 'True'
SECRET_KEY = os.getenv('SECRET_KEY', 'change-me-in-production!')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

# Database Configuration
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# Static Files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security Headers
SECURE_SSL_REDIRECT = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_SECURITY_POLICY = {
    "default-src": ("'self'",),
    "script-src": ("'self'", "'unsafe-inline'", "cdn.jsdelivr.net"),
    "style-src": ("'self'", "'unsafe-inline'", "cdn.jsdelivr.net"),
    "img-src": ("'self'", "data:", "https:"),
}

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### Step 5: Set Up Gunicorn

Create `gunicorn_config.py`:

```python
# gunicorn_config.py

import multiprocessing

# Server Socket
bind = "0.0.0.0:8000"
backlog = 2048

# Worker Processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process Naming
proc_name = 'teaching-platform'

# Server Hooks
def on_starting(server):
    print("Gunicorn server is starting...")

def when_ready(server):
    print("Gunicorn server is ready. Spawning workers")
```

Run Gunicorn:

```bash
gunicorn config.wsgi:application --config gunicorn_config.py
```

---

## Server Configuration

### Nginx Configuration

Create `/etc/nginx/sites-available/teaching-platform`:

```nginx
upstream django {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;
    
    # SSL Configuration
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    
    # SSL Settings
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
    
    client_max_body_size 20M;
    
    # Static Files
    location /static/ {
        alias /var/www/teaching-platform/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
    
    # Media Files
    location /media/ {
        alias /var/www/teaching-platform/media/;
        expires 7d;
        add_header Cache-Control "public";
    }
    
    # Django Application
    location / {
        proxy_pass http://django;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
        
        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
    
    # Security Headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "DENY" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
}
```

Enable the site:

```bash
sudo ln -s /etc/nginx/sites-available/teaching-platform /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Enable SSL with Let's Encrypt

```bash
sudo apt-get install certbot python3-certbot-nginx
sudo certbot certonly --nginx -d yourdomain.com -d www.yourdomain.com
```

### Systemd Service for Gunicorn

Create `/etc/systemd/system/teaching-platform.service`:

```ini
[Unit]
Description=Teaching Platform Gunicorn Application
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/teaching-platform

Environment="PATH=/var/www/teaching-platform/venv/bin"
ExecStart=/var/www/teaching-platform/venv/bin/gunicorn \
    --workers 4 \
    --worker-class sync \
    --bind 127.0.0.1:8000 \
    --timeout 60 \
    config.wsgi:application

Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable teaching-platform
sudo systemctl start teaching-platform
sudo systemctl status teaching-platform
```

---

## Environment Variables

Create `.env` file in project root:

```env
# Django Settings
DEBUG=False
SECRET_KEY=your-secure-random-key-here
ENVIRONMENT=production

# Allowed Hosts
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/teaching_platform

# Email Configuration (Optional)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password

# Redis (Optional)
REDIS_URL=redis://127.0.0.1:6379/1

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

Load environment variables in `settings.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG', 'False') == 'True'
SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')
```

---

## Security Checklist

- [ ] Set `DEBUG = False` in production
- [ ] Generate a strong `SECRET_KEY` (use `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Set `SECURE_SSL_REDIRECT = True`
- [ ] Set `SESSION_COOKIE_SECURE = True`
- [ ] Set `CSRF_COOKIE_SECURE = True`
- [ ] Use PostgreSQL instead of SQLite
- [ ] Enable HTTPS/SSL
- [ ] Configure proper database backups
- [ ] Set up monitoring and logging
- [ ] Use environment variables for sensitive data
- [ ] Run `python manage.py check --deploy`
- [ ] Set up firewall rules
- [ ] Keep dependencies updated
- [ ] Configure rate limiting
- [ ] Set up database backups
- [ ] Configure error logging/monitoring (Sentry, etc.)

---

## Heroku Deployment (Quick Start)

### Step 1: Install Heroku CLI

```bash
# Download and install from https://devcenter.heroku.com/articles/heroku-cli
```

### Step 2: Create Heroku App

```bash
heroku login
heroku create your-app-name
```

### Step 3: Add PostgreSQL Add-on

```bash
heroku addons:create heroku-postgresql:mini
```

### Step 4: Set Environment Variables

```bash
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
```

### Step 5: Create Procfile

Create `Procfile` in project root:

```
web: gunicorn config.wsgi:application
release: python manage.py migrate
```

### Step 6: Create runtime.txt

Create `runtime.txt`:

```
python-3.11.0
```

### Step 7: Deploy

```bash
git add .
git commit -m "Prepare for Heroku deployment"
git push heroku main
heroku run python manage.py createsuperuser
```

Access your app at `https://your-app-name.herokuapp.com`

---

## Performance Optimization

### Enable Caching

```python
# settings.py

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### Database Optimization

```python
# Use select_related and prefetch_related in querysets
# Example:
articles = Article.objects.prefetch_related('media_items', 'sections')
```

### Static File Compression

```python
# settings.py
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

---

## Troubleshooting

### Issue: Static files not loading

```bash
# Collect static files again
python manage.py collectstatic --clear --noinput

# Check permissions
sudo chown -R www-data:www-data /var/www/teaching-platform/staticfiles
```

### Issue: Database connection errors

```bash
# Check PostgreSQL is running
sudo systemctl status postgresql

# Test database connection
python manage.py dbshell
```

### Issue: Permission denied errors

```bash
# Fix file permissions
sudo chown -R www-data:www-data /var/www/teaching-platform
sudo chmod -R 755 /var/www/teaching-platform
```

### Issue: Gunicorn not starting

```bash
# Check logs
journalctl -u teaching-platform -n 50
sudo journalctl -u teaching-platform -f
```

### Issue: Nginx errors

```bash
# Test Nginx configuration
sudo nginx -t

# Check logs
sudo tail -f /var/log/nginx/error.log
```

---

## Maintenance

### Regular Tasks

```bash
# Check Django system health
python manage.py check --deploy

# Update dependencies
pip install --upgrade -r requirements.txt

# Clean up old files
python manage.py clearsessions

# Backup database
pg_dump teaching_platform > backup_$(date +%Y%m%d_%H%M%S).sql
```

### Database Backups

```bash
# Manual backup
pg_dump -U teaching_user teaching_platform > backup.sql

# Automated daily backup (cron job)
# Add to crontab: 0 2 * * * pg_dump -U teaching_user teaching_platform > /backups/teaching_platform_$(date +\%Y\%m\%d).sql
```

---

## Support

For issues or questions:
- Check [README.md](README.md) for general information
- Review [debugLog.md](debugLog.md) for debugging information
- Check application logs in `/var/log/teaching-platform/` or `journalctl`

