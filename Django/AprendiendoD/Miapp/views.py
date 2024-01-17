from django.shortcuts import render, HttpResponse

# Create your views here
# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

def index(request):
    return render(request,'index.html')
def holaMundo(request):
    return render(request, 'holaMundo.html')
def pagina(request):
    return render(request, 'pagina.html')
