from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("유저 정보", {"fields":("email","nickname","is_business","password")}),
        ("Premissions", {"fields":("is_active","is_staff","is_superuser")},)
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','nickname','is_business','password1','password2'),
        }),
    )

    list_display = ('email','nickname','is_business','is_active','is_staff')
    search_fields = ('email','nickname')
    ordering = ('email',)
