from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def sheru(request):
    return HttpResponse("Aiiit... Kya haal chal")
def greet(request, name):
    return render(request, "hello/greet.html" , {
        "name" : name.capitalize()
    })