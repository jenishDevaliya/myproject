# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
]
