from django.contrib import admin

from .models import Account, Category, Transaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Register Account Model in AdminPanel"""
    list_display = ['user', 'first_name', 'last_name', 'balance']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Register Category Model in AdminPanel"""
    list_display = ['title']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Register Transaction Model in AdminPanel"""
    list_display = ['type_of_transaction', 'user', 'category', 'amount', 'date']
