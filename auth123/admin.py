from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomAdminModel(UserAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'comment',
    )

admin.site.register(CustomUser, CustomAdminModel)
