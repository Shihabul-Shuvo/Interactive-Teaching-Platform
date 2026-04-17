# Database Migrations Guide

## Overview

The Interactive Teaching Platform uses Django migrations to manage database schema changes. Migrations are automatically generated based on changes to the models in `apps/content/models.py`.

## Creating New Migrations

When you modify a model:

```bash
# Create new migration files
python manage.py makemigrations

# View what changes will be applied
python manage.py sqlmigrate apps.content 0001

# Apply migrations to database
python manage.py migrate
```

## Current Models

### MediaItem
- `id`: Primary key
- `title`: CharField (max 200)
- `media_type`: CharField (choices: text, image, audio, video, youtube)
- `description`: TextField (optional)
- `file`: FileField (optional, upload_to='media_files/')
- `youtube_url`: URLField (optional)
- `created_at`: DateTimeField (auto_now_add)

### Article
- `id`: Primary key
- `title`: CharField (max 300)
- `subtitle`: CharField (max 500, optional)
- `slug`: SlugField (unique)
- `body`: TextField
- `is_active`: BooleanField (default=True)
- `created_at`: DateTimeField (auto_now_add)
- `updated_at`: DateTimeField (auto_now)

### Section
- `id`: Primary key
- `article`: ForeignKey to Article (cascade)
- `section_type`: CharField (choices: introduction, detailed, resources)
- `title`: CharField (max 200)
- `content`: TextField
- `order`: PositiveSmallIntegerField
- `created_at`: DateTimeField (auto_now_add)

### Term
- `id`: Primary key
- `slug`: SlugField (unique)
- `label`: CharField (max 100)
- `media_item`: ForeignKey to MediaItem (nullable, cascade)
- `created_at`: DateTimeField (auto_now_add)

### MediaInteraction
- `id`: Primary key
- `media_item`: ForeignKey to MediaItem (cascade)
- `user_agent`: TextField
- `ip_address`: GenericIPAddressField (optional)
- `timestamp`: DateTimeField (auto_now_add)

## Migration Workflow

### First Time Setup

```bash
# Apply all pending migrations
python manage.py migrate
```

This will create all tables in your database.

### After Modifying Models

```bash
# 1. Make changes to models.py
# 2. Create migration files
python manage.py makemigrations

# 3. Review the migration (optional)
python manage.py showmigrations

# 4. Apply migrations
python manage.py migrate

# 5. Verify changes
python manage.py dbshell
```

### Reversing Migrations

If you need to rollback:

```bash
# Rollback to previous migration
python manage.py migrate apps.content 0001

# Rollback all migrations for an app
python manage.py migrate apps.content zero
```

## Database Operations

### Backup Database

```bash
# SQLite
cp db.sqlite3 db.sqlite3.backup

# PostgreSQL
pg_dump teaching_platform > backup.sql
```

### Reset Database (Development Only)

```bash
# Remove all data and reapply migrations
python manage.py flush --no-input
python manage.py migrate

# Reload sample data
python manage.py load_sample_data
```

### Import Sample Data

```bash
python manage.py load_sample_data
```

## Troubleshooting

### Migration Conflicts

If you have conflicting migrations:

```bash
# Check migration status
python manage.py showmigrations

# Merge migrations
python manage.py makemigrations --merge
```

### Missing Migrations

```bash
# Recreate migrations
python manage.py makemigrations

# Show what would change
python manage.py migrate --plan
```

### Database Lock (SQLite)

If you get "database is locked" errors:

```bash
# Wait for connections to close
# Or delete db.sqlite3 and start fresh
rm db.sqlite3
python manage.py migrate
python manage.py load_sample_data
```

## PostgreSQL Setup

For production, use PostgreSQL:

```bash
# Install PostgreSQL
# Create database
createdb teaching_platform

# Update settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'teaching_platform',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Install psycopg2
pip install psycopg2-binary

# Apply migrations
python manage.py migrate
```

## Best Practices

✅ **Always:**
- Review migration files before applying
- Test migrations on development first
- Backup database before major migrations
- Use meaningful migration names
- Document schema changes in commit messages

❌ **Never:**
- Manually edit migration files
- Use `DROP TABLE` in production
- Skip migrations in deployment
- Delete migration files

## Additional Resources

- [Django Migrations Documentation](https://docs.djangoproject.com/en/5.0/topics/migrations/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
