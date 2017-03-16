from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'category': category_list}
    return render(request,'rango/index.html',context_dict)
#def index(request):
#    context_dict = {'boldmessage':"i am bold font "}
#    return render(request, 'rango/index.html',context_dict)
#    #return HttpResponse("Rango says hey F*ck")

def about(request):
    return HttpResponse("Rango Hello<br/> <a href='/rango/about'>About Page</a>")
#    return HttpResponse("Rango About Page!!")

def category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['cate'] = category
    except Category.DoesNotExist:
        pass
    return render(request,'rango/category.html',context_dict)
