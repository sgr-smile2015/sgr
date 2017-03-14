from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage':"i am bold font "}
    return render(request, 'rango/index.html',context_dict)
    #return HttpResponse("Rango says hey F*ck")

def about(request):
    return HttpResponse("Rango Hello<br/> <a href='/rango/about'>About Page</a>")
#    return HttpResponse("Rango About Page!!")
