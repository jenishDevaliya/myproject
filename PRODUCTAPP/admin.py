from django.contrib import admin
from .models import Category, Product, CartItem, Order  # Ensure these models are correctly imported


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock')
    list_filter = ('category',)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'ordered_at')

# Register your models here
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
