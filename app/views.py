from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import CustomUser
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionAPIView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return object for current authenticated user only"""
        return self.queryset.filter(user=self.request.user)

# class TransactionAPIView(generics.RetrieveUpdateAPIView):
#     """Detail. to put and patch pk should be in urls"""
#     serializer_class = TransactionSerializer
#     permission_classes = (IsAuthenticated, )
#     queryset = Transaction.objects.all()
#
#     def get_queryset(self):
#         """Return object for current authenticated user only"""
#         return self.queryset.filter(user=self.request.user)
