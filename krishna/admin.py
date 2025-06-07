# krishna/admin.py
from django.contrib import admin
from .models import UserModel

class UserModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email')  # Display the fields in the admin list view
    search_fields = ('name', 'number', 'email')  # Enable searching by these fields
    list_filter = ('number', 'email')  # Add filters for these fields

admin.site.register(UserModel, UserModelAdmin)
