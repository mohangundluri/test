from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view() , name='home'),
    path('delete/<int:pk>/', views.delete_data, name= 'delete'),
    path('update/<int:pk>/', views.Update.as_view(), name='update'),
    path('delete/', views.delete_all, name="delete_all"),
]