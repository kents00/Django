from django.shortcuts import render
from django.http import request

# Create your views here.

def Menu(request):
    return render(request, 'layout/main.html')