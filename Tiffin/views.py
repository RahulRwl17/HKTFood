from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Tiffin.models import Order
# Create your views here.

def Home(request):
    messages.success(request,"Welcome To HKT...!")
    return render(request,'index.html')

def About(request):
    return render(request,'Aboutus.html')

def order(request):
    if request.method == "POST":
        cname = request.POST.get('cus_name')
        nt = request.POST.get('no')
        date = request.POST.get('time')
        payment = request.POST.get('customCheck1')
        tgive = request.POST.get('customCheck2')
        trecv = request.POST.get('customCheck3')
        odr = Order(cname=cname,nt=nt,date=date,payment=payment,tgive=tgive,trecv=trecv)
        print(payment)
        odr.save()
        messages.success(request,"Order Has Been Placed..!")
       
    return render(request,'Order.html')