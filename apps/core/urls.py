from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='article-detail'),
]
