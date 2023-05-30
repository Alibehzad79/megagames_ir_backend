from django.contrib import admin
from ads_app.models import ArticleDetailPageAds, HomePageAds, TagPageAds, CategoryPageAds, SearchPageAds
# Register your models here.

@admin.register(ArticleDetailPageAds)
class ArticleDetailPageAdsAdmin(admin.ModelAdmin):
    list_display = ('client', 'article', 'date_start', 'date_end', 'active')
    list_editable = ('active',)
    list_filter = ('date_start', 'date_end', 'active')
    search_fields = ('client', 'article', 'url')
    
    

@admin.register(HomePageAds)
class HomePageAdsAdmin(admin.ModelAdmin):
    list_display = ('client', 'date_start', 'date_end', 'active')
    list_editable = ('active',)
    list_filter = ('date_start', 'date_end', 'active')
    search_fields = ('client', 'article', 'url')


@admin.register(TagPageAds)
class TagPageAdsAdmin(admin.ModelAdmin):
    list_display = ('client', 'tag', 'date_start', 'date_end', 'active')
    list_editable = ('active',)
    list_filter = ('date_start', 'date_end', 'active')
    search_fields = ('client', 'article', 'url')        
    
@admin.register(CategoryPageAds)
class CategoryPageAdsAdmin(admin.ModelAdmin):
    list_display = ('client', 'category', 'date_start', 'date_end', 'active')
    list_editable = ('active',)
    list_filter = ('date_start', 'date_end', 'active')
    search_fields = ('client', 'article', 'url')
    

@admin.register(SearchPageAds)
class SearchPageAdsAdmin(admin.ModelAdmin):
    list_display = ('client', 'date_start', 'date_end', 'active')
    list_editable = ('active',)
    list_filter = ('date_start', 'date_end', 'active')
    search_fields = ('client', 'article', 'url')    