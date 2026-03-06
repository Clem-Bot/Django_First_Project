from django.shortcuts import render, HttpResponse
from django.contrib import admin
from django.urls import path

# Create your views here.
def index(request):
    return render(request, 'polls/index.html')
