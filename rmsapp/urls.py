from django.urls import path
from . import views

urlpatterns = [
    
 
    path('', views.home, name="home"),
    path('create_request/', views.create_request, name="create_request"),
    path('customer', views.customer, name="customer"),
    path('service', views.service, name="service"),
    path('create_request/', views.create_request, name="create_request"),
    path('chart', views.chart, name="chart"),
    path('edit/<str:pk>/', views.edit, name="edit"),
    path('delete/<str:pk>/', views.delete, name="delete"),
    path('delete_service/<str:pk>/', views.delete_service, name="delete_service"),
    
    
    
    
    
    

    
]