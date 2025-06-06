from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={
        'name':'Suprim',
        'age':21,
        'nationality':'Nepalese'
    }
    return render(request,'index.html',context)