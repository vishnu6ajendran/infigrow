from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import InfigrowUser

class CustomUserAdmin(UserAdmin):
    model = InfigrowUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff']

admin.site.register(InfigrowUser, CustomUserAdmin)