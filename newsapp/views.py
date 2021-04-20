from django.shortcuts import render

from .models import Story


def index(request):
    return render(request, 'newsapp/index.html')


def news(request):
    latest_news_list = Story.objects.order_by('pub_date')
    context = {
        'latest_news_list': latest_news_list,
    }
    return render(request, 'newsapp/news.html', context)
