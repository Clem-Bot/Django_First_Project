from django.shortcuts import render, HttpResponse
from django.contrib import admin
from django.urls import path

# Create your views here.
def home(request):
    thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}   
    context = {'abcd':thisdict} 
    
    return render(request, 'appone/home.html', context)
def services(request):
    return render(request, 'appone/services.html')
def about(request):
    return render(request, 'appone/about.html')
def contact(request):
    return render(request, 'appone/contact.html')