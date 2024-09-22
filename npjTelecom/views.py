from django.shortcuts import render, HttpResponse
from .models import Avenger

# Create your views here.

def index(request):
    data = Avenger.objects.all()
    return render(request, "npjTelecom/index.html",{"data":data})

def contact(request):
    return render(request, "npjTelecom/contact.html")

def about(request):
    return render(request, "npjTelecom/about.html")

def service(request):
    return render(request, "npjTelecom/service.html")


