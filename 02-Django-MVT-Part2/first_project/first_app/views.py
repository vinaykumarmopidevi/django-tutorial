from django.shortcuts import render
from django.http import HttpResponse 
from .models import Product
from .models import User
from .models import Employee
from .models import Department
from .models import Table1
from .models import Table2
# Create your views here.
def index(request):
    #return HttpResponse("Hello world")
    my_dict={'data':'Flask_app_development'}
    return render(request,'sample/index.html',my_dict)

def product_list(request):
    #read
    products = Product.objects.all()
    return render(request, 'products/products_list.html', {'products': products})

def users(request):
    #update
    #data=User.objects.filter(id=1)
    #data.update(first_name='rama')
    #delete
    #data=User.objects.filter(id=1)
    #data.delete()
    #read
    user_list=User.objects.order_by('first_name')
    return render(request,"usersinfo/users.html",context={"users":user_list})


def emp_info(request):
    emp_list = Employee.objects.all().select_related('department') \
      .values('id', 'name','address', 'id', 'name','department__id','department__name')
    return render(request,'empinfo/emp_list.html',{'emp_data':emp_list})


def table_info(request):
   # q_list=Table2.objects.all().select_related('locker')
    q_list = Table2.objects.all().select_related('locker') \
      .values('locker__locker_id', 'locker__locker_name',
                   'locker__city', 'locker__state', 'locker__pincode',
                   'locker__locker_capacity', 'key', 'empty_slots')
    return render(request,'tableinfo/table_list.html',{'table_data':q_list})

