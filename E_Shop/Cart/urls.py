from django.urls import path

from .views import *

urlpatterns = [
    path('Add_To_Cart/<int:id>/',Add_To_Cart,name='Add_To_Cart')
    
  
]