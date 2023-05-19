from django.contrib import admin
from blog_app.models import Article, Tag ,Category ,Gallery ,Downloadbox ,Comment

# Register your models here.

class GalleryInline(admin.TabularInline):
    model = Gallery
    
class DownloadboxInline(admin.TabularInline):
    model = Downloadbox


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'id_post' ,'title' ,'category' ,'date_created' ,'view_visit', 'active')
    inlines = [GalleryInline, DownloadboxInline]
    list_editable = ('active',)
    list_filter = ('active', 'date_created', 'category__name', 'category__slug', 'tags')
    search_fields = ('title', 'content', 'id_post', 'category__name', 'category__slug', 'tags__name', 'tags__slug')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_send', 'status')
    list_filter = ('status', 'date_send')
    list_editable = ('status',)
    search_fields = ('name', 'email', 'text', 'article__title')

admin.site.register(Category)
admin.site.register(Tag)  
