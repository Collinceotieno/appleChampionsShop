from django.shortcuts import render, redirect
from pyexpat.errors import messages
from django.contrib import messages

from products.forms import ProductForm
from .models import Product


def products(request):
    all_products = Product.objects.all()
    context = {"products": all_products}
    return render(request, 'products/products.html', context)


def add_products(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product saved successfully')
        else:
            messages.error(request, 'Product saving failed')
            return redirect("add-products-url")
    else:
        form = ProductForm()
    return render(request, 'products/add-products.html', {'form': form})


def update_products(request):
    return render(request, 'products/update-products.html')


def shop(request):
    return render(request, 'products/shop.html')
