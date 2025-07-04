from django.shortcuts import render
from .models import Transactions
from rest_framework.response import Response
from .searilizers import TransactionsSerializers

# Create your views here.

def get_transactions(request):
    queryset =Transactions.objects.all()
    serializer = TransactionsSerializers(queryset, many=True)

    return Response({
        "data":serializer.data
    })
