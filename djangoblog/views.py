from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'base_layout.html')

def about(request):
    return render(request, 'about.html')

