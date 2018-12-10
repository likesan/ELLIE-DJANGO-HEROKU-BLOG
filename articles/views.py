from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def article_list(request):
    articles = Article.objects.filter(position=2).order_by('date') # all articles
    headers = Article.objects.filter(position=3).order_by('date') # collect only header position posts
    return render(request, 'articles/article_list.html', {'articles':articles, 'headers':headers})

def article_detail(request, slug):
    print(request, slug)    
    article = Article.objects.get(slug=slug)
    return render(request,"articles/article_detail.html", {'article':article})   
    
