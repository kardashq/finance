import uuid
import os

from django.db import models
from django.conf import settings


def customer_image_file_path(filename):
    """Generate file path for new image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('upload/customer/', filename)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to=customer_image_file_path)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Account(models.Model):
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )

    moneybox = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT  # we cannot delete user with balance
    )

    def __str__(self):
        return f'{self.id} of {self.user.username}'


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    TRANSACTION_TYPE_CHOICES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    type_of_transaction = models.CharField(
        choices=TRANSACTION_TYPE_CHOICES,
        max_length=8
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f'{self.amount} - {self.user}'