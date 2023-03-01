from rest_framework import serializers

from .models import Transaction, Account


class TransactionSerializer(serializers.ModelSerializer):
    """All transaction for """
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'category', 'amount', 'type_of_transaction', 'date',)


class AccountSerializer(serializers.ModelSerializer):
    """Account details"""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Account
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):
    """Serializer for CRUD operations with transactions"""

    class Meta:
        model = Transaction
        fields = ('id', 'category', 'amount', 'description', 'type_of_transaction', 'date', 'account')
        read_only_fields = ('id', 'date', 'account')

    def create(self, validated_data):
        """Create new transaction"""
        print(validated_data)
        if validated_data['type_of_transaction'] == 'income':
            validated_data['account'].balance += validated_data['amount']
            validated_data['account'].save()
        elif validated_data['type_of_transaction'] == 'expense':
            validated_data['account'].balance -= validated_data['amount']
            validated_data['account'].save()
        return super(ActionSerializer, self).create(validated_data)
