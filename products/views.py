from django.shortcuts import render
from django.http import response
from .models import Product
from .forms import ProductCreateForm

# Create your views here.


def product_view(request, *args, **kwargs):
    prod_one = Product.objects.get(id=1)
    context = {
        'title': prod_one.title,
        'description': prod_one.description
    }
    return render(request, "product.html", context)


def product_form_view(request):
    form = ProductCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
    context = {
        'form': form
    }

    return render(request, "form.html", context)
