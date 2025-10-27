
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'city', 'country', 'postal_code', 'date_of_birth')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'phone_number', 'address', 'city', 'country', 'postal_code', 'date_of_birth')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)