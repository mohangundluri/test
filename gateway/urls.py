from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="payment"),
    path('payment-status/', views.payment_status, name='payment-status')
]