from django.contrib import admin

from UserApp.models import UserModel

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['name','email','contact']
    list_filter=['contact']

admin_site.register(UserModel,UserAdmin) 