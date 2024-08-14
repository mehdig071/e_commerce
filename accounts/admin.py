from django.contrib import admin
from accounts.models.Customer import Customer
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'agree_terms', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    
    
admin.site.register(Customer, CustomUserAdmin)