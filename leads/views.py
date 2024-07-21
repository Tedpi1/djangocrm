from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

def home(request):
    #return HttpResponse("Hello World")
    return render(request, "leads/home.html")
# Create your views here.
