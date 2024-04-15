from django.db import models

# Create your models here.
class Department(models.Model):
    dept_id=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=120)

    def __str__(self):
        return self.dept_name
    
class Employee(models.Model):
    emp_name=models.CharField(max_length=120)
    address=models.CharField(max_length=120)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name

