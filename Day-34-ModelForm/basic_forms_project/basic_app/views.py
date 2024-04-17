from django.shortcuts import render
from . import signUp
from .signUp import ProductForm

# Create your views here.
def index(request):
    return render(request,"index.html")

def form_name_view(request):
    form=signUp.FormName()

    if request.method == 'POST':
        form = signUp.FormName(request.POST)

        if form.is_valid():
            print("Validation successful")  
            print(f"the name: {form.cleaned_data['name']}")
        else:
            print("Validation failed")

    return render(request,"signUp.html",{"form":form})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request) 
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})