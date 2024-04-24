# Django RestAPI Example

create a Django REST API using Django REST Framework (DRF):

1. **Setup Django Project**:
   First, make sure you have Django and Django REST Framework installed. You can install them using pip:

   ```bash
   pip install django djangorestframework
   ```

   Then, create a new Django project and navigate to its directory:

   ```bash
   django-admin startproject myproject
   cd myproject
   ```

2. **Create a Django App**:
   Create a new Django app within your project:

   ```bash
   python manage.py startapp myapp
   ```

3. **Define Models**:
   Open `myapp/models.py` and define a simple model, for example:

   ```python
   from django.db import models

   class Book(models.Model):
       title = models.CharField(max_length=100)
       author = models.CharField(max_length=100)
       published_date = models.DateField()

       def __str__(self):
           return self.title
   ```

4. **Create Serializers**:
   Create serializers to convert model instances to JSON format. In `myapp/serializers.py`:

   ```python
   from rest_framework import serializers
   from .models import Book

   class BookSerializer(serializers.ModelSerializer):
       class Meta:
           model = Book
           fields = '__all__'
   ```

5. **Create Views**:
   Define API views using Django REST Framework's class-based views. In `myapp/views.py`:

   ```python
   from rest_framework import viewsets
   from .models import Book
   from .serializers import BookSerializer

   class BookViewSet(viewsets.ModelViewSet):
       queryset = Book.objects.all()
       serializer_class = BookSerializer
   ```

6. **Configure URLs**:
   Configure URLs to map API endpoints to views. In `myproject/urls.py`:

   ```python
   from django.urls import include, path
   from rest_framework import routers
   from myapp.views import BookViewSet

   router = routers.DefaultRouter()
   router.register(r'books', BookViewSet)

   urlpatterns = [
       path('', include(router.urls)),
   ]
   ```

7. **Run Migrations**:
   Apply migrations to create the database schema for your models:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. **Run Development Server**:
   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

Now you can access your REST API at `http://127.0.0.1:8000/books/`, where you can perform CRUD operations (Create, Read, Update, Delete) on your `Book` model.