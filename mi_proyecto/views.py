from django.http import HttpResponse

def saludo(request):
    return HttpResponse ("¡Hola, Bienvenidos a Django!")