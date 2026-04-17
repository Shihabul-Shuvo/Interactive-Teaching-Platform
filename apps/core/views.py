from django.shortcuts import render
from django.views import View
from apps.content.models import Article


class IndexView(View):
    """
    Renders the main index page.
    Displays a list of all active articles as a listing.
    """
    def get(self, request):
        # Filter for active articles with non-empty slugs
        articles = Article.objects.filter(
            is_active=True,
            slug__isnull=False
        ).exclude(
            slug=''
        ).prefetch_related('sections')
        context = {
            'articles': articles,
        }
        return render(request, 'core/index.html', context)


class ArticleDetailView(View):
    """
    Renders a single article with:
    - Purple gradient hero header (title + subtitle)
    - Left column: multimedia content examples (clickable badges)
    - Left column: article body with interactive terms
    - Right sidebar: expandable accordion sections
    """
    def get(self, request, slug):
        try:
            article = Article.objects.prefetch_related(
                'sections'
            ).get(slug=slug, is_active=True)
        except Article.DoesNotExist:
            return render(request, 'core/404.html', status=404)
        
        context = {
            'article': article,
            'sections': article.sections.all(),
        }
        return render(request, 'core/article_detail.html', context)
