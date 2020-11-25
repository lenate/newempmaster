from django.shortcuts import render,HttpResponse,render,redirect
from .models import Employees

def home(request):
    return render(request,"empfirst.html")

def add(request):
    
   
    if request.method=="GET":
         return render(request,'empadd.html')
    else:
        prop=Employees()
        prop.ename=request.POST.get('ename')
        prop.address=request.POST.get('address')
        prop.phone=request.POST.get('phone')
        prop.email=request.POST.get('email')
        
        prop.image=request.FILES['img']
        
        prop.save()
        return redirect(home)


