from django.contrib.sitemaps import Sitemap
from blog_app.models import Article


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Article.objects.filter(active=True).all()

    def lastmod(self, obj):
        return obj.date_created