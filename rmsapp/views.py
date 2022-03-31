from datetime import datetime
from urllib import request
from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponse
from .forms import RequestForm, ServiceForm,CustomerForm
from .filters import RequestFilter




#----------Dashboard View --------------

def home(request):
   customers = Customer.objects.all()
   services = Service.objects.all()

      
   labels = []
   data = []
   q = Service.objects.all()   
   for s in q :
        labels.append(s.name)
        data.append(s.services)

   
   requests = Request.objects.all().order_by('-created_date')[0:5]
   total_requests = Request.objects.all().count()
   total_WIP = Request.objects.filter(status = 'Work In Progress').count()
   total_P_C = Request.objects.filter(status = 'Pending Customer').count()
   total_Completed = Request.objects.filter(status = 'Completed').count()
   total_Rejected = Request.objects.filter(status = 'Rejected').count()

   context = {'data':data,'labels':labels,'total_P_C':total_P_C,'total_Completed':total_Completed,'total_Rejected':total_Rejected,'total_WIP':total_WIP,'total_requests':total_requests,'requests':requests,'customers':customers,'services':services }
   
   return render (request,'rmsapp/dashboard.html',context) 



#---------- Create Request  --------------

def create_request(request):
       
    form = RequestForm()
    
    if request.method == 'POST':
       form = RequestForm(request.POST) 
       if form.is_valid():
           form.save()
           return redirect('/')   
        
    context = {'form': form}
    return render (request, 'rmsapp/create_request.html', context)


#----------Edit  --------------
 
def edit(request, pk):
       
    customer_request = Request.objects.get(id=pk)
    form = RequestForm(instance=customer_request)
   
    if request.method == 'POST':
         form = RequestForm(request.POST, instance=customer_request)
         if form.is_valid():
            form.save()
            return redirect('/')  
    context = {'form':form}
    return render (request, 'rmsapp/edit.html', context)


#----------Delete  Requests --------------

def delete (request, pk):
   customer_request = Request.objects.get(id=pk)  
   
   customer_ = customer_request.customer.name
   if request.method == 'POST':
      customer_request.delete()
      return redirect ('/')
   
   
   context = { 'customer_request': customer_request,'customer_':customer_}
   return render(request,'rmsapp/delete.html',context)

#-----------Delete Services ---------------- 

def delete_service (request, pk):
    service_request = Service.objects.get(id=pk)
    if request.method == 'POST':
       service_request.delete()    
       return redirect ('/')
   
   
    context = {'service_request':service_request}
    return render(request,'rmsapp/delete_service.html',context)










#----------Service Page  View --------------

def service(request):
    services= Service.objects.all()


   #-----chart.js------------

  
    form = ServiceForm()
    if request.method == 'POST':
       form = ServiceForm(request.POST)
       if form.is_valid:
          form.save()
          return redirect ('/')    
   
    context = {'form':form,'services':services}
 
    return render (request,'rmsapp/service.html',context)
 
 
 
 
 #----------Customer Page  View --------------

def customer(request):
    customers = Customer.objects.all()
    requests  = Request.objects.all()
 
   #---------- Filter Customer --------------
 
    form_filter = RequestFilter(request.GET, queryset=requests)
    requests = form_filter.qs
    
   #----------Customer Form--------------
  
    form = CustomerForm()
    if request.method == 'POST':
       form =CustomerForm(request.POST)
       if form.is_valid:
          form.save()
          return redirect ('/')    
  
  
    context = {'form':form,'form_filter':form_filter,'requests':requests,'customers':customers}
    return render (request,'rmsapp/customer.html', context)





#---------- Chart.JS  --------------

def chart (request):
    context = {}
    return render (request,'rmsapp/chart.html',context)
 
 
