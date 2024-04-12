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
```

Running `python manage.py migrate` in a Django project applies any pending database migrations to synchronize the database schema with the current state of your project's models. Here's what happens when you run this command:

1. **Checks for Unapplied Migrations**: Django keeps track of which migrations have been applied to your database and which ones are pending. When you run `migrate`, Django checks for any unapplied migrations.

2. **Applies Pending Migrations**: If there are pending migrations, Django applies them in the order they were created. Each migration contains instructions for modifying the database schema, such as creating or altering tables, adding or removing columns, or creating indexes.

3. **Updates the `django_migrations` Table**: After applying migrations, Django updates its internal records in the `django_migrations` table to reflect that these migrations have been applied. This table serves as a record of which migrations have been executed.

4. **Ensures Database Consistency**: `migrate` ensures that the database schema matches the models defined in your Django project. It performs database operations safely and efficiently, handling various database engines and their specific requirements.

5. **No Action if No Migrations Pending**: If there are no pending migrations, running `migrate` will simply output "No migrations to apply" and won't make any changes to the database.

Overall, `python manage.py migrate` is a crucial command for keeping your database schema in sync with your Django project's models. It's typically run after making changes to your models or after pulling changes from collaborators that include new migrations.

Running `python manage.py makemigrations` in a Django project analyzes the current state of your models and creates migration files that represent the changes you've made to your models since the last migration. Here's what happens when you run this command:

1. **Analyzes Models**: Django inspects all the models defined in your project's apps, comparing them to the existing database schema.

2. **Detects Changes**: It detects any changes you've made to your models since the last migration. This includes additions, deletions, or alterations to fields, as well as changes in relationships between models.

3. **Generates Migration Files**: Django creates migration files for each app in your project where changes have been detected. These migration files are Python scripts that contain instructions for how to apply the changes to the database schema. They are stored in the `migrations` directory of each app.

4. **Includes Descriptions of Changes**: Each migration file includes a series of operations (such as creating, altering, or deleting tables and fields) necessary to bring the database schema in line with the current state of the models.

5. **Doesn't Modify the Database**: `makemigrations` only generates migration files; it doesn't actually modify the database schema. This allows you to review and customize the generated migrations before applying them to your database using `python manage.py migrate`.

6. **Creates a Dependency Graph**: Django also creates a dependency graph between migrations, ensuring that migrations are applied in the correct order to maintain database consistency.

Overall, `python manage.py makemigrations` is a crucial step in the Django migration workflow. It helps you manage changes to your models in a structured way and ensures that your database schema evolves alongside your project's codebase.

**Create Superuser:**

```sh
python manage.py createsuperuser
```

```sh
pip install Faker
```

**Fake data generate:**

```python
import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
# Import settings
django.setup()

import random
from first_app.models import Product
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.name()
        fake_price = fakegen.pyint()
        fake_description = fakegen.name()

        # Create new User Entry
        user = Product.objects.get_or_create(name=fake_name,
                                          price=fake_price,
                                          description=fake_description)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
```