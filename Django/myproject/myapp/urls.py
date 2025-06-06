from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name='index'),   # views.py is imported as views and index is the function
    path("counter/",views.counter,name='counter')    #use / after
]