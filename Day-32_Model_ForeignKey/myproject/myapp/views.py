from django.shortcuts import render
from .models import Employee
from .models import Department

# Create your views here.
def index(request):
    return render(request,"index.html")

def emp_info(request):
    emp_list=Employee.objects.all().select_related('department')\
        .values('id','emp_name','address','department__dept_id','department__dept_name')
    return render(request,"emp_info/emp_list.html",{"emp_list":emp_list})
