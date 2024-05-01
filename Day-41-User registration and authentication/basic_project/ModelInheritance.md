In Django, model inheritance is a powerful feature that allows you to create new models based on existing ones, inheriting fields and behavior. There are three main types of model inheritance in Django:

1. **Abstract Base Classes**: These are base classes from which other models can inherit fields and methods, but no database table is created for the base class itself.

2. **Multi-table Inheritance**: Each model in the hierarchy is a separate model with its own database table. Child models have all the fields of their parent model plus any additional fields defined in the child model.

3. **Proxy Models**: These are essentially mirrors of the original model. They allow you to modify the Python-level behavior of the model without changing its fields or the data stored in its table.

Here's a brief overview of each:

1. **Abstract Base Classes**:
   
   ```python
   from django.db import models
   
   class Base(models.Model):
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   
       class Meta:
           abstract = True
   
   class Child(Base):
       name = models.CharField(max_length=100)
   ```

2. **Multi-table Inheritance**:

   ```python
   from django.db import models
   
   class Parent(models.Model):
       parent_field = models.CharField(max_length=100)
   
   class Child(Parent):
       child_field = models.CharField(max_length=100)
   ```

3. **Proxy Models**:

   ```python
   from django.db import models
   
   class Parent(models.Model):
       name = models.CharField(max_length=100)
   
   class Child(Parent):
       class Meta:
           proxy = True
   
       def do_something(self):
           return f"Something with {self.name}"
   ```

Each type of inheritance has its own use cases and implications, so choose the one that best fits your requirements. Remember to consider database schema implications, query behavior, and code organization when deciding which type of inheritance to use.