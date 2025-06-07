from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from .models import Cart, CartItem  # Assuming Cart and CartItem are defined in accounts.models


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def home_view(request):
    return render(request, 'accounts/home.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)  # Make sure ProductModel is imported correctly
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        # If the item already exists, increase the quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')


@login_required
def remove_from_cart(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.delete()
    return redirect('view_cart')


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'accounts/cart.html', {'cart_items': cart_items})


def product_list(request):
    products = ProductModel.objects.all()  # Querying ProductModel to get all products
    return render(request, 'product_list.html', {'products': products})
