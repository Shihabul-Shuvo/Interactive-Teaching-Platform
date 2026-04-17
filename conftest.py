"""
pytest configuration for the Interactive Teaching Platform.
"""

import os
import django
from django.conf import settings

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

if not settings.configured:
    django.setup()

import pytest
from django.test import Client
from django.contrib.auth.models import User


@pytest.fixture
def client():
    """Provide a Django test client."""
    return Client()


@pytest.fixture
def admin_user(db):
    """Create an admin user for tests."""
    return User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='testpass123'
    )


@pytest.fixture
def regular_user(db):
    """Create a regular user for tests."""
    return User.objects.create_user(
        username='testuser',
        email='user@example.com',
        password='testpass123'
    )


@pytest.fixture
def authenticated_client(client, admin_user):
    """Provide an authenticated test client."""
    client.login(username='admin', password='testpass123')
    return client
