from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .form import ProductForm
from .models import Product


# Create your views here.
def index(request):
    context={}
    return render(request,"index.html",context=context)

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request) 
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def products(request):
    context={"products":Product.objects.all()}
    return render(request,"product_list.html",context=context)

def product_details(request,pk):
    product=get_object_or_404(Product,pk=pk)
    context={'product':product}
    return render(request,"product_details.html",context=context)

def redirect_me(request):
    return redirect(reverse('basic_app:product_list'))

def redirect_value(request):
    return redirect(reverse('basic_app:product_details',kwargs={'pk':2}))

    