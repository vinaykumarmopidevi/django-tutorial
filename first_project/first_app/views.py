from django.shortcuts import render
from django.http import HttpResponse 
from .models import Product

# Create your views here.
def index(request):
    #return HttpResponse("Hello world")
    my_dict={'data':'Flask_app_development'}
    return render(request,'sample/index.html',my_dict)

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/products_list.html', {'products': products})
