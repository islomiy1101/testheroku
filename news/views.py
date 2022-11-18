from django.shortcuts import render

from news.models import *
def home(request):
    posts=Article.objects.all()
    context={
        'posts':posts
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def article_detail(request,slug):
    article=Article.objects.get(slug=slug)
    context={
        'article':article
    }
    return render(request,'article_detail.html',context)