from django.shortcuts import render, HttpResponse
from .models import Avenger

# Create your views here.

def index(request):
    data = Avenger.objects.all()
    return render(request, "npjTelecom/index.html",{"data":data})
