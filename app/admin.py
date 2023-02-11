from django.contrib import admin

from models import (Customer, Account,
                    Category, Transaction)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Register Customer Model in AdminPanel"""
    list_display = ['first_name', 'last_name']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Register Account Model in AdminPanel"""
    list_display = ['balance', 'moneybox']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Register Category Model in AdminPanel"""
    list_display = ['title']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Register Transaction Model in AdminPanel"""
    list_display = ['type_of_transaction', 'user', 'category', 'amount', 'date']
