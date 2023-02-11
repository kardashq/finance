from django.contrib import admin

from models import (Customer, Account,
                    Category, Transaction)


@admin.register(Customer)
"""Register CustomerModel in admin"""
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['balance', 'moneybox']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['type_of_transaction', 'user', 'category', 'amount', 'date']
