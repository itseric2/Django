from django.http import HttpResponse
import datetime
from django.template import Template, Context

def holamundo(request): # Función Vista - Primera vista
    
    doc_externo = open("C:/Users/TOSHIBA/Desktop/Django-projects/First/First/plantillas")
    
    plt = Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx = Context()
    
    documento = plt.render(ctx)
    
    return HttpResponse(documento)


def mrd(request):
    
    return HttpResponse("kkk")

def fecha(request):
    
    fecha_actual = datetime.datetime.now()
    
    documentof = """<html>
    <body>
    <h3>
    Fecha y Hora actuales %s
    </h3>
    </body>
    </html>""" % fecha_actual
    
    return HttpResponse(documentof)

def cedad(request, edad, ano):
    
    #edadactual = 16
    tiempo = ano-2024
    edadfutura = edad+tiempo
    documentoce = """<html>
    <body>
    <h3>
    En el año %s tendras %s años
    </h3>
    </body>
    </html>""" %(ano, edadfutura)
    
    return HttpResponse(documentoce)