from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'full_name', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('id','username','email', 'full_name', 'is_staff', 'last_login', 'registered_at')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username','email',)
    ordering = ('-registered_at',)
    filter_horizontal = ('groups', 'user_permissions',)
    list_display_link = ('username','full_name')

admin.site.register(User, UserAdmin)