from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import Transaction, Account
from .serializers import AccountSerializer, ActionSerializer, TransactionSerializer


class TransactionsAPIView(generics.ListAPIView):
    """Endpoint for view all transactions """
    queryset = Transaction.objects.all()
    authentication_classes = (TokenAuthentication, )
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """Return object for current authenticated user only"""
        print(self.request.user)
        return self.queryset.filter(account__user=self.request.user)


class AccountDetail(generics.RetrieveUpdateAPIView):
    """Endpoint for get and put, auth user is used
    for filter"""
    serializer_class = AccountSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Account.objects.all()

    def get_object(self):
        return self.queryset.filter(user=self.request.user).first()


class ActionViewSet(viewsets.GenericViewSet,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    """Endpoint for CRUD operation for transaction"""
    serializer_class = ActionSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Transaction.objects.all()

    def perform_create(self, serializer):
        """Create new transaction"""
        account = get_object_or_404(Account, user=self.request.user)
        return serializer.save(account=account)

    def get_queryset(self):
        """Return object for current authenticated user only"""
        return self.queryset.filter(account__user=self.request.user)
