from rest_framework import serializers
from .models import Transactions

class TransactionsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Transactions
        fields=[
            "title",
            "amount",
            "transaction_type",
        ]

        '''Use fields="__all__" to include all fields '''