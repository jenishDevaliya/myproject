from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User  # Import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add any other fields necessary for the Cart model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Cart of {self.user.username}'


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

    def get_total_price(self):
        return self.product.price * self.quantity  # Total price of the CartItem


class Order(models.Model):
    cart_items = models.ManyToManyField(CartItem)
    ordered_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return sum(item.get_total_price() for item in self.cart_items.all())

    def __str__(self):
        return f"Order {self.id} - Total: ${self.total_price}"
class AccountCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account_cart')  # Keep or change related_name

    def __str__(self):
        return f"{self.user.username}'s Account Cart"


        