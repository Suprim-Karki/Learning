from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),   # views.py is imported as views and index is the function
    path('counter',views.counter,name='counter'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]