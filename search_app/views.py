from django.shortcuts import render
from search_app.models import SaerchResault
from blog_app.models import Article
# Create your views here.

def search(request):
    template_name = 'base/search_result.html'
    query = request.GET.get('q')
    if query is not None:
        articles = Article.objects.get_by_search(query=query)
        if not SaerchResault.objects.filter(query_name=query).exists():
            SaerchResault.objects.create(query_name=query, research_count=1)
        else:
            q = SaerchResault.objects.get(query_name=query)
            q.research_count += 1
            q.save()
    else:
        articles = Article.objects.filter(active=True).all()
    
    context = {
        'query': query,
        'articles': articles
    }
    
    return render(request, template_name, context)