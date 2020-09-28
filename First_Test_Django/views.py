from django.shortcuts import render, redirect
from blog.models import Article

def index (request):
    article= Article.objects.all

    return render(request, 'blog/HTML/Main.index.html',{'derniers_articles':article})