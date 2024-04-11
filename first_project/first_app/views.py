from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def help(request):
    help_dict = {'help_insert':'HELP PAGE'}
    return render(request,'first_app/help.html',context=help_dict)

def index(request):
    return render(request,'first_app/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'first_app/users.html',context=user_dict)