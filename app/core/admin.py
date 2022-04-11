from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class MyUserAdmin(UserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']


admin.site.register(User, MyUserAdmin)
