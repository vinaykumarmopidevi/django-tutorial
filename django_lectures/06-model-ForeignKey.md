# ForeignKey

***model***

```python
class Department(models.Model):
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
      .values('id', 'name','address', 'id', 'name','department__id','department__name')
    return render(request,'empinfo/emp_list.html',{'emp_data':emp_list})
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
            <li>department id: {{ emp.department__id }}</li>
            <li>Department Name: {{ emp.department__name }}</li>
        </ul>
        {% endfor %}
    </ol>
    {% endif %}
</body>
</html>
```