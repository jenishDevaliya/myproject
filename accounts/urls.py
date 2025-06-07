from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),                # Home page
    path('signup/', views.signup, name='signup'),          # Signup page
    path('login/', views.user_login, name='login'),        # Login page
    path('logout/', views.logout, name='logout'),          # Logout functionality
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),      # Add to cart
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),  # Remove from cart
    path('cart/', views.view_cart, name='view_cart'),      # View cart
    path('products/', views.product_list, name='product_list'),  # Product list URL
]
