In Django, `ModelForm` is a powerful tool provided by the Django framework for creating forms based on models. It's a form class that inherits from `django.forms.ModelForm` and is automatically generated from a Django model. Using `ModelForm`, you can quickly create forms that allow users to create, update, and delete model instances.

Here's a basic example of how you might use `ModelForm`:

Suppose you have a Django model called `Product`:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

You can create a form for this model using `ModelForm`:

```python
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
```

In this `ProductForm` class:

- `Meta` inner class is used to specify metadata about the form.
- `model` attribute is set to the `Product` model, indicating which model the form is based on.
- `fields` attribute lists the fields from the `Product` model that you want to include in the form.

With this `ProductForm` class, you can now create, update, and delete `Product` instances using HTML forms. For example, in a Django view function or class-based view, you could use this form to handle form submissions and interact with the database:

```python
from django.shortcuts import render, redirect
from .forms import ProductForm

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to a page showing list of products
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})
```

In the above example, when the form is submitted, `form.save()` is called to save the data to the database if the form data is valid.

Overall, `ModelForm` is a convenient way to create forms in Django that are tied to specific models, allowing you to easily work with model data in your views and templates.