from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    # products=Offer.objects.all()
    return render(request,'home.html')

def index(request):
    products=Product.objects.all()
    return render(request,'index.html',{'data':products})

def men(request):
    products=Offer.objects.all()
    return render(request,'men.html',{'data':products})

def child(request):
    products=kids.objects.all()
    return render(request,'kids.html',{'data':products})


