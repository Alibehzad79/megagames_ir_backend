from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from blog_app.models import Article, Comment, Category, Tag
from blog_app.forms import CommentForm
from datetime import datetime
from ads_app.models import ArticleDetailPageAds
# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = "base/base.html"
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(active=True).all()

def article_detail(request, *args, **kwargs):
    template_name = 'base/detail.html'
    pk = kwargs['pk']
    article = get_object_or_404(Article.objects.filter(id=pk))
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')
            new_comment = Comment.objects.create(article=article, name=name, email=email, text=text, date_send=datetime.now(), status=False)
            if new_comment is not None:
                return redirect('article_detail', article.id, article.title)
    else:
        form = CommentForm()
    related_posts = Article.objects.filter(category=article.category).distinct().all()[:4]
    ads = ArticleDetailPageAds.objects.filter(active=True, article=article).all()
    today_ads = None
    for ad in ads:
        if ad.date_start <= datetime.today().date() <= ad.date_end:
            today_ads = ad

    article.view_visit += 1
    article.save()
    context = {
        'article': article,
        'form': form,
        'related_posts': related_posts,
        'today_ads': today_ads,
    }
    
    return render(request, template_name, context)


def article_detail_2(request, *args, **kwargs):
    pk = kwargs['id_post']
    article = get_object_or_404(Article.objects.filter(id_post=pk))
    return redirect('article_detail', article.id, article.title)

def get_article_by_category(request, *args, **kwargs):
    template_name = "base/search_result.html"
    category_slug = kwargs['category_slug']
    article = Article.objects.filter(category__slug=category_slug, active=True).all()
    category = Category.objects.filter(slug=category_slug).last()
    category.visit_count += 1
    category.save()
    context = {
        'articles': article,
        'category': category,
    }
    return render(request, template_name, context)


def get_article_by_tag(request, *args, **kwargs):
    template_name = "base/search_result.html"
    tag_slug = kwargs['tag_slug']
    article = Article.objects.filter(tags__slug=tag_slug, active=True).all()
    tag = Tag.objects.filter(slug=tag_slug).last()
    tag.visit_count += 1
    tag.save()
    context = {
        'articles': article,
        'tag': tag,
    }
    return render(request, template_name, context)




# TODO ads system for tags, categories, search_app, home_page