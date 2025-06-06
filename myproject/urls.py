# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('productapp/', include('PRODUCTAPP.urls')),  # Include the accounts URLs
]
