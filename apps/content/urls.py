from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MediaItemViewSet, ArticleViewSet, TermDetailView

router = DefaultRouter()
router.register(r'media-items', MediaItemViewSet, basename='mediaitem')
router.register(r'articles',    ArticleViewSet,   basename='article')

urlpatterns = [
    path('', include(router.urls)),
    path('terms/<slug:slug>/', TermDetailView.as_view(), name='term-detail'),
]