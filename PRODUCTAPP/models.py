from django.db import models
from django.contrib.auth.models import User  # Import User model

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)  # Ensure this field is present
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_cart')  # Unique related_name

    def __str__(self):
        return f"{self.user.username}'s Cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')  # Reference to Cart model
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

    def get_total_price(self):
        return self.product.price * self.quantity  # Total price of the CartItem

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')  # Related name for user orders
    cart_items = models.ManyToManyField(CartItem)
    ordered_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return sum(item.get_total_price() for item in self.cart_items.all())

    def __str__(self):
        return f"Order {self.id} by {self.user.username} - Total: ${self.total_price:.2f}"
