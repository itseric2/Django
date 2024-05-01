from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render

def prueba(request):
    
    return render(request, "prototype.html")