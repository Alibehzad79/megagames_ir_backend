"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from config import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from blog_app.views import ArticleListView, article_detail, article_detail_2, get_article_by_category, get_article_by_tag
from search_app.views import search
from settings_app.views import contact, ads
from blog_app.sitemap import BlogSitemap

sitemaps = {
    "blog_app": BlogSitemap,
}

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('articles/<int:pk>/<slug:slug>/', article_detail, name='article_detail'),
    path('articles/<id_post>/', article_detail_2, name='article_detail_2'),
    path('search/', search, name='search'),
    path('category/<slug:category_slug>/', get_article_by_category, name='category'),
    path('tag/<slug:tag_slug>/', get_article_by_tag, name='tag'),
    path('contact/', contact, name='contact'),
    path('ads/', ads, name='ads'),
    path(
        "sitemap.xml/",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)