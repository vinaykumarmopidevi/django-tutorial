from django.shortcuts import render
from .models import Band

# Create your views here.
def index(request):
    bonds= Band.objects.filter(genre='Punk')

    return render(request,"index.html",context={"bonds":bonds})