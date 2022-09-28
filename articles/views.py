from multiprocessing import context
import random
from django.shortcuts import render, redirect
from .models import Article   # 같은 폴더 내에 있는 파일이기 때문에

# Create your views here.

def index(request):
    return render(request, 'index.html')


def dinner(request, name):
    menus = [
        {'name':'한식', 'price':12000}, 
        {'name':'일식', 'price':20000}, 
        {'name':'양식', 'price':20000}, 
        {'name':'분식', 'price':8000}, 
    ]

    pick = random.choice(menus)
    articles = Article.objects.order_by('-pk')
    context = {
        'pick' : pick,
        'name' : name,
        'menus' : menus,
        'articles' : articles
    }
    return render(request, 'dinner.html', context)


def review(request):
    return render(request, 'review.html')


def create_review(request):
    content = request.POST.get('content')
    title = request.POST.get('title')
    article = Article(title=title, content=content)
    article.save()

    return redirect('/articles/dinner/list')