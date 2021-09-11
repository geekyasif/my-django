from django.shortcuts import render,HttpResponse, reverse
from .models import Post , Category

# Create your views here.

def home(request):
    post = Post.objects.order_by("-timestamp")
    category = Category.objects.all()
    context = {
        'post': post,
        'category': category
    }
    return render(request, 'home.html', context)

def blogPost(request, post_slug,category_slug):
    post = Post.objects.get(slug = post_slug)
    cat = Category.objects.get(slug = category_slug)

    context = {
        'post' : post,
        'cat' : cat,
    }

    return render(request, 'blogPost.html', context)

def category(request, cat_slug):
    category1 = Category.objects.get(slug = cat_slug)
    context = {
         'category1' : category1
    }
    return render(request, 'category.html', context)

# def categoryPost(request, cat_slug, post_slug):
#     post = 

