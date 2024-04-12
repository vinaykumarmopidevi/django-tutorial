from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def index(request):
    my_dict={'name':'django'}
    return render(request,'products/index.html',context=my_dict)