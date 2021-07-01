from django.shortcuts import render
from django.http import response
from .models import Product

# Create your views here.


def product_view(request, *args, **kwargs):
    prod_one = Product.objects.get(id=1)
    context = {
        'title': prod_one.title,
        'description': prod_one.description
    }
    return render(request, "product.html", context)
