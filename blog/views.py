from django.shortcuts import render, get_object_or_404
from .models import Article, Category

# Create your views here.
def home(request):
    context = {
        'articles': Article.objects.filter(status='p'),
    }
    return render(request, 'blog/home.html', context)


def category_list(request):
    context = {
        'categories': Category.objects.filter(status=True),
    }
    return render(request, 'blog/category_list.html', context)


def category_detail(request, slug):
    context = {
        'category': get_object_or_404(Category, slug=slug, status=True)
    }
    return render(request, 'blog/category_detail.html', context)
    

def article(request, slug):
    context = {
        'article': get_object_or_404(Article, slug=slug, status='p')
    }
    return render(request, 'blog/article.html', context)


def contact(request):
    return render(request, 'blog/contact.html')


def about(request):
    return render(request, 'blog/about.html')