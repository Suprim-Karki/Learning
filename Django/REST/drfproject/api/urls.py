from django.urls import path
from drfapp import views

urlpatterns = [
    path('get-transactions',views.get_transactions)
]
