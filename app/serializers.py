from rest_framework import serializers

from .models import Transaction, Account


class TransactionSerializer(serializers.ModelSerializer):
    """Вывод всех операций"""
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'category', 'amount', 'type_of_transaction',)


class AccountSerializer(serializers.ModelSerializer):
    """Вывод данных аккаунта"""

    class Meta:
        model = Account
        fields = ('__all__')
        #exclude = ('user',)


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'account', 'category', 'amount', 'description', 'type_of_transaction', 'date')
        read_only_fields = ('id', 'date', 'account')

    def create(self, validated_data):
        print(validated_data)
        if validated_data['type_of_transaction'] == 'income':
            validated_data['account'].balance += validated_data['amount']
            validated_data['account'].save()
        elif validated_data['type_of_transaction'] == 'expense':
            validated_data['account'].balance -= validated_data['amount']
            validated_data['account'].save()
        return super(ActionSerializer, self).create(validated_data)
