from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Speed'
    # feature1.details = 'We are very fast'

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Accurate'
    # feature2.details = 'We are very accurate'

    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Reliability'
    # feature3.details = 'We are very reliable'

    # features=[feature1,feature2,feature3]

    features=Feature.objects.all()

    return render(request,'index.html',{'features':features})

def counter(request):
    text=request.POST['text']  #words is the name of the input textbox 
    no_of_words=len(text.split())
    return render(request,'counter.html',{'text':text,'no_of_words':no_of_words})