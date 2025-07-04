from django.shortcuts import render
from .models import Transactions
from rest_framework.response import Response
from .searilizers import TransactionsSerializers
from rest_framework.decorators import api_view


@api_view()
def get_transactions(request):
    queryset =Transactions.objects.all()
    serializer = TransactionsSerializers(queryset, many=True)

    return Response({
        "data":serializer.data
    })
