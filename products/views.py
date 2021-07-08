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
    print(request)
    my_new_title = request.POST.get('title')
    print(my_new_title)

    return render(request, "form.html", {})
