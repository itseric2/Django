from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render

def prueba(request):
    
    doc_externo = open("C:/Users/TOSHIBA/Desktop/Django-projects/First/First/Web-Preview/prototype.html")
    
    plt = Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx = Context()
    
    documento = plt.render(ctx)
    
    return HttpResponse(documento)

def prueba2(request):
    
    doc_externo2 = open("C:/Users/TOSHIBA/Desktop/Django-projects/First/First/Web-Preview/registro.html")
    
    plt = Template(doc_externo2.read())
    
    doc_externo2.close()
    
    ctx = Context({"grados": [f"{i}-{j}" for i in range(5, 12) for j in range(1, 8)]})
    
    documento2 = plt.render(ctx)
    
    return HttpResponse(documento2)