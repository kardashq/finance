from djoser.signals import user_registered
from django.dispatch import receiver

from .models import Account


@receiver(user_registered, dispatch_uid="create_account")
def create_account(sender, user, request, **kwargs):
    """Signal to create an account upon registration"""
    data = request.data

    Account.objects.create(
        user=user,
        first_name=data.get("first_name", ""),
        last_name=data.get("last_name", "")
    )
