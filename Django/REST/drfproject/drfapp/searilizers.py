from rest_framework import serializers
from .models import Transactions

class TransactionsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Transactions
        fields=[
            "title",
            "amoune",
            "transaction_type",
        ]
