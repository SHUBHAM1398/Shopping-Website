from django.shortcuts import render,HttpResponse
from datetime import datetime
from app1.models import Contact
from app1.models import About
from django.contrib import messages
#shubham admin and password is shubham@123
# Create your views here.
def index(request):
    context ={
        "variable1":"SB-website"
    }

    return render(request,'index.htm',context)
    #  return HttpResponse("this is home page")
def services(request):
    return render(request,'services.htm')
def about(request):
    if request.method =="POST":
        email=request.POST.get('email')
        feedback=request.POST.get('feedback')
        about=About(email=email ,feedback=feedback)
        about.save()
        messages.success(request, 'Your feedback is submitted!')
    return render(request,'about.htm')
   # return HttpResponse("this is service page")
def contact(request):
    if request.method =="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        password= request.POST.get('password')
        address= request.POST.get('address')
        city= request.POST.get('city')
        state= request.POST.get('state')
        contact= Contact(name=name,email=email,password=password,address=address,city=city,state=state,date=datetime.today())
        contact.save()
        messages.success(request, 'Your data is submitted!')
    return render(request,'contact.htm')
    #return HttpResponse("this is contact page")