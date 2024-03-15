from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Product

def add_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        Product.objects.create(product_id=product_id, product_name=product_name)
        return render(request, 'add_product.html')
    return render(request, 'add_product.html')
