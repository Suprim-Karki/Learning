from django.shortcuts import render
from .models import Transactions
from rest_framework.response import Response
from .searilizers import TransactionsSerializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView


@api_view(["GET","POST"])
def get_transactions(request):
    queryset =Transactions.objects.all()
    serializer = TransactionsSerializers(queryset, many=True)

    return Response({
        "data":serializer.data
    })


class TransactionsAPI(APIView):
    def get(self,response):     #for get method
        return Response({
            "message":"this is a get method"
        })
    
    def post(self,response):     #for post method
        return Response({
            "message":"this is a post method"
        })
    def put(self,response):     #for put method
        return Response({
            "message":"this is a put method"
        })
    def patch(self,response):     #for patch method
        return Response({
            "message":"this is a patch method"
        })