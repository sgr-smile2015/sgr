#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey F*ck")

def about(request):
    return HttpResponse("Rango Hello<br/> <a href='/rango/about'>About Page</a>")
#    return HttpResponse("Rango About Page!!")
