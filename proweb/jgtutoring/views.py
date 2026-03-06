from django.shortcuts import render, HttpResponse
from django.contrib import admin
from django.urls import path
# Create your views here.

def tutor(request):
    return render(request, 'jgtutoring/tutor.html')
