from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.


def home(request):
    # allProducts = Product.objects.all()
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # allProducts = [[products, range(1, nSlides), nSlides], [
    #     products, range(1, nSlides), nSlides]]
    allProducts = []
    product_category = Product.objects.values('category')
    categories = {item['category'] for item in product_category}
    for category in categories:
        products = Product.objects.filter(category=category)
        n = len(products)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProducts.append([products, range(1, nSlides), nSlides])

    context = {
        'products' :products,
        'range' : range(1,nSlides),
        'no_of_slides' : nSlides,
    }
    context = {
        'allProducts': allProducts
    }
    return render(request, 'ecom/index.html', context)


def product_detail(request, category, sub_category, product_slug):
    product = Product.objects.get(product_slug = product_slug, category = category, sub_category = sub_category )
    context = {
        'product' : product
    }
    return render(request, 'ecom/product_detail.html', context)


def checkout(request):
    pass


def tracker(request):
    pass


def search(request):
    pass


def about(request):
    pass


def contact(request):
    pass
