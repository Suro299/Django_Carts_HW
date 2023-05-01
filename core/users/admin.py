from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "email", "is_staff", "is_active")
    list_filter = ("username", "email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "email", "password",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions", "cart_prod")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", "cart_prod"
            )}
        ),
    )
    search_fields = ("email", "username")
    ordering = ("username", "is_staff")


admin.site.register(CustomUser, CustomUserAdmin)