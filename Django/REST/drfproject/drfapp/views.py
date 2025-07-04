from django.shortcuts import render
from .models import Transactions
from rest_framework.response import Response
# Create your views here.

def get_transactions(request):
    query=Transactions.objects.all()

    return Response()
