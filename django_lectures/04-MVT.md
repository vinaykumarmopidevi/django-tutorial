# Model-View-Template

MVT stands for Model-View-Template, which is the architectural pattern used in Django web application development. Here's a breakdown of each component:

1. **Model:** This is where you define the structure of your data. Models in Django are Python classes that represent database tables. They define fields and behaviors of the data you're storing. Django's ORM (Object-Relational Mapper) helps you interact with the database using these models without writing SQL queries directly.

2. **View:** Views are Python functions or classes that receive web requests and return web responses. In Django, views are responsible for processing user input, interacting with the models to fetch or manipulate data, and then rendering the appropriate templates to generate HTML responses.

3. **Template:** Templates are HTML files that define the presentation layer of your web application. They contain placeholders and template tags that Django's template engine processes to dynamically generate the final HTML sent to the client's browser. Templates can include logic using template tags and filters, making it easy to create dynamic and reusable HTML content.

In summary, MVT separates the concerns of data (Model), logic (View), and presentation (Template) in Django applications, promoting a clean and organized structure for building web applications.

## Example to illustrate the MVT pattern in Django web application development

1. **Model (models.py):**

   ```python
   from django.db import models

   class Product(models.Model):
       name = models.CharField(max_length=255)
       price = models.DecimalField(max_digits=10, decimal_places=2)
       description = models.TextField()

       def __str__(self):
           return self.name
   ```

2. **View (views.py):**

   ```python
   from django.shortcuts import render
   from .models import Product

   def product_list(request):
       products = Product.objects.all()
       return render(request, 'products/product_list.html', {'products': products})
   ```

3. **Template (product_list.html):**

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Product List</title>
   </head>
   <body>
       <h1>Products</h1>
       <ul>
           {% for product in products %}
               <li>{{ product.name }} - ${{ product.price }}</li>
           {% endfor %}
       </ul>
   </body>
   </html>
   ```

In this example:

- **Model:** We define a `Product` model with fields like `name`, `price`, and `description`.
- **View:** The `product_list` view fetches all products from the database using `Product.objects.all()` and passes them to the template for rendering.
- **Template:** The `product_list.html` template displays a list of products using a for loop to iterate over the products passed from the view.

This structure adheres to the MVT pattern in Django, where models define data, views handle logic and data processing, and templates handle presentation and rendering

**admin (admin.py):**

 ```python
from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.register(Product)
```

**app url (url.py):**

```python
from django.urls import path
from . import views

urlpatterns = [
   path('products/', views.product_list, name="products"),
]

```

**Project url (url.py):**

```python
from django.contrib import admin
from django.urls import path,include
from first_app import views

urlpatterns = [
    path('',include('first_app.urls')),
    path("admin/", admin.site.urls),
]

```

**Database migration:**

```sh
python manage.py migrate
python manage.py makemigrations first_app
python manage.py migrate
python manage.py createsuperuser
```

**Create Superuser:**

```sh
python manage.py createsuperuser
```
