from django.shortcuts import render
from .models import Product  # Ensure this matches the name in models.py

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def product_view(request):
    return render(request, 'product.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})
