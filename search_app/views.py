from django.shortcuts import render
from search_app.models import SaerchResault
from blog_app.models import Article
from ads_app.models import SearchPageAds
from datetime import datetime
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
    ads = SearchPageAds.objects.filter(active=True).all()
    today_ads = None
    for ad in ads:
        if ad.date_start <= datetime.today().date() <= ad.date_end:
            today_ads = ad
    context = {
        'query': query,
        'articles': articles,
        'today_ads': today_ads,
    }
    
    return render(request, template_name, context)