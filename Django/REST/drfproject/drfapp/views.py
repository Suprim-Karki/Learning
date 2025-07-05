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
    def get(self,request):     #for get method
        return Response({
            "message":"this is a get method"
        })
    
    def post(self,request):     #for post method
        data=request.data        #to send data go to postman, post, body, raw, and input data
        serializer = TransactionsSerializers(data=data)
        if not serializer.is_valid():     #data will only go to server if is_valid() is called
            return Response({
                "message":"data not saved",
                "errors": serializer.errors,
            })
        serializer.save()
        return Response({
            "message":"this is a post method",
            "data":serializer.data
        })
    def put(self,request):     #for put method
        return Response({
            "message":"this is a put method"
        })
    def patch(self,request):     #for patch method
        data=request.data        

        if not data.get("id"):
            return Response({
                "message":"data not updated",
                "errors":"id is required"
            })
        
        transactions=Transactions.objects.get(id = data.get("id"))
        serializer = TransactionsSerializers(transactions,data=data,partial=True)

        if not serializer.is_valid():     
            return Response({
                "message":"data not updated",
                "errors": serializer.errors,
            })
        serializer.save()
        return Response({
            "message":"data updated",
            "data":serializer.data
        })