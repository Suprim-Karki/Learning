from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

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

def register(request):
    if request.method!= 'POST':
        return render(request,'register.html')
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    password2=request.POST['password2']

    if username=="" or email=="" or password=="":
        messages.info(request, 'Fill in all fields')
        return render(request,'register.html')

    if password!=password2:
        messages.info(request, 'Passwords are not matching')
        return redirect('register')
    
    if User.objects.filter(email=email).exists():
        messages.info(request, 'Email already exists')
        return redirect('register')
    
    if User.objects.filter(username=username).exists():
        messages.info(request, 'Username already exists')
        return redirect('register')
    
    user=User.objects.create_user(username=username,email=email, password=password)
    user.save()

def login(request):
    return render(request,'login.html')
