from rest_framework import serializers
from .models import Transactions

class TransactionsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Transactions

        '''To include fields you want'''
        fields=[
            "id",
            "title",
            "amount",
            "transaction_type",
        ]

        '''To include all fields '''
        # fields="__all__"

        '''To exclude certain fields and include all others'''
        # exclude=[
        #     'amount',
        #     'transaction_type',
        # ]