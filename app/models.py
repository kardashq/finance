import uuid
import os

from django.db import models
from django.conf import settings


def customer_image_file_path(instanse, filename):
    """Generate file path for new image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('upload/customer/', filename)


class Account(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to=customer_image_file_path)
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    TRANSACTION_TYPE_CHOICES = (
        ('income', 'Доход'),
        ('expense', 'Расход'),
    )

    type_of_transaction = models.CharField(
        choices=TRANSACTION_TYPE_CHOICES,
        max_length=8
    )

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='actions',
    )

    def __str__(self):
        return f'{self.amount} - {self.account}'
