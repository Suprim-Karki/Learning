from django.shortcuts import render
from .models import Transactions
# Create your views here.

def get_transactions(request):
    query=Transactions.objects.all()
    