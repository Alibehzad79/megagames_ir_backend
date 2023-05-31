from django.shortcuts import render
from blog_app.models import Category
from settings_app.models import Setting
from blog_app.models import Article
from datetime import datetime

def header(request):
    template_name = 'base/header.html'
    categories = Category.objects.all()
    setting = Setting.objects.last()
    context = {
        'categories': categories,
        'setting': setting,
    }
    return render(request, template_name, context)


def footer(request):
    template_name = 'base/footer.html'
    articles = Article.objects.filter(active=True).all()[:13]
    setting = Setting.objects.last()
    date = datetime.now()
    context = {
        'articles': articles,
        'setting': setting,
        'date': date,
    }
    return render(request, template_name, context)