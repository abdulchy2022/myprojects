from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

    @property
    def requests(self):
        request_count = self.request_set.all().count()
        return str(request_count)
                  
class Service  (models.Model):
    
    NAME = (
        
        ('Desktop','Desktop'),
        ('Network','Network'),
        ('Backup','Backup'),
        ('CyberSecurity','CyberSecurity')
            )
    name = models.CharField(max_length=200, null=True, choices = NAME)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    @property
    def services(self):
        service_count = self.request_set.all().count()
        return str(service_count)    
     

class Request  (models.Model):
    STATUS = (
        
        ('Pending Customer','Pending Customer'),
        ('Work In Progress','Work In Progress'),
        ('Completed','Completed'),
        ('Rejected','Rejected')
        
             )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True,null= True) 
    status = models.CharField(max_length=200, null= True, choices= STATUS ) 
     
    def __str__ (self):
         return self.service.name