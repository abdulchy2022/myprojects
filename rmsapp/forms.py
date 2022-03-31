
import django

from django.forms import ModelForm
from .models import *


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = '__all__'
        


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields ='__all__'
        
        
        
        
        
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields ='__all__'
        