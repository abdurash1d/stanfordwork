from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from .forms import UserAdminChangeForm, UserAdminCreationForm

from apps.users.models import (Resume, 
                     Student)

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    list_display = ('email', 'is_superuser', 'is_active')
    list_filter = ('is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, UserAdmin)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Resume model.
    """
    list_display = ('user', 'file', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('user__username', 'user__email')
    ordering = ('-uploaded_at',)

admin.site.unregister(Group)

@admin.register(Group)
class CustomGroupAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Group model.
    """
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Permission model.
    """
    list_display = ('name', 'codename', 'content_type')
    search_fields = ('name', 'codename')
    list_filter = ('content_type',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user')
    search_fields = ('first_name', 'last_name', 'user__username')
    