from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles':articles} )
# third arguments are the data what I wish to deliever to the html template! It's like the JSP from Frontcontroller in Java Springs

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug) # get the article title/slug/etc which is the included slug is same which is gotten through the url slug
    return render(request,"articles/article_detail.html",{'article':article})