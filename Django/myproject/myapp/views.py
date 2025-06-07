from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    return render(request,'index.html')

def counter(request):
    text=request.POST['text']  #words is the name of the input textbox 
    no_of_words=len(text.split())
    return render(request,'counter.html',{'text':text,'no_of_words':no_of_words})