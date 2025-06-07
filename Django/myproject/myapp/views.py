from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Speed'
    feature1.details = 'We are very fast'
    return render(request,'index.html',{'feature':feature1})

def counter(request):
    text=request.POST['text']  #words is the name of the input textbox 
    no_of_words=len(text.split())
    return render(request,'counter.html',{'text':text,'no_of_words':no_of_words})