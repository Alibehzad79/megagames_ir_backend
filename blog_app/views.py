from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from blog_app.models import Article
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
    
    context = {
        'article': article,
    }
    
    return render(request, template_name, context)


def article_detail_2(request, *args, **kwargs):
    pk = kwargs['id_post']
    article = get_object_or_404(Article.objects.filter(id_post=pk))
    return redirect('article_detail', article.id, article.title)
