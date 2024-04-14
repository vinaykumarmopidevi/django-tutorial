# ForeignKey

```sql
SELECT *
FROM first_app_employee
INNER JOIN  first_app_department
ON first_app_employee.department_id=first_app_department.dept_id;
```

***model***

```python
from django.db import models

# Create your models here.
class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=70)
    address=models.CharField(max_length=90)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
```

***view***

```python
def emp_info(request):
    emp_list = Employee.objects.all().select_related('department') \
      .values('id', 'name','address','department__dept_id','department__name')
    return render(request,'empinfo/emp_list.html',{'emp_data':emp_list})
```

```python
from django.contrib import admin
from .models import Department
from .models import Employee


# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)
```

```python
from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('empInfo/', views.emp_info, name="emp_info"),
]
```

***template***

```html
<!DOCTYPE html>
<html>
<head>
    <title>Employee Page</title>
</head>
<body>
    <h1>Employees</h1>
   
    {% if emp_data %}
    <ol>
        {% for emp in emp_data %}
        <li>Employee Info</li>
        <ul>
            <li>Emp Id: {{ emp.id }}</li>
            <li>Name: {{ emp.name }}</li>
            <li>Address: {{ emp.address }}</li>
            <li>department id: {{ emp.department__dept_id }}</li>
            <li>Department Name: {{ emp.department__name }}</li>
        </ul>
        {% endfor %}
    </ol>
    {% endif %}
</body>
</html>
```
