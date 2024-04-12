# Django Templates

Django templates in Python are a key part of the Django web framework, used for generating dynamic HTML content. Here are the basics of working with Django templates:

1. **Template Syntax:**
   Django templates use a special syntax for inserting variables, tags, and filters into HTML files. Variables are enclosed in double curly braces `{{ variable }}`, tags in curly braces with percent signs `{% tag %}`, and filters are applied using pipe `|` after a variable or tag. For example:

   ```html
   <p>Hello, {{ user.username }}!</p>
   {% if user.is_authenticated %}
       <p>Welcome back!</p>
   {% else %}
       <p>Please log in.</p>
   {% endif %}
   ```

2. **Context and Rendering:**
   In Django, views pass data to templates through a context dictionary. This context is then used to render the template with the appropriate data. Here's an example view and template rendering in Django:

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse
   from .models import Product

   def product_detail(request, product_id):
       product = Product.objects.get(id=product_id)
       context = {'product': product}
       return render(request, 'product_detail.html', context)
   ```

   In the `product_detail.html` template:

   ```html
   <h1>{{ product.name }}</h1>
   <p>Price: ${{ product.price }}</p>
   ```

3. **Template Inheritance:**
   Django templates support inheritance, allowing you to create base templates with common elements and extend them in child templates. This helps in maintaining consistent layouts across multiple pages. For example, a base template (`base.html`) might look like this:

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>{% block title %}My Site{% endblock %}</title>
   </head>
   <body>
       {% block content %}
       {% endblock %}
   </body>
   </html>
   ```

   And a child template (`home.html`) extending the base template:

   ```html
   {% extends 'base.html' %}

   {% block title %}Home - My Site{% endblock %}

   {% block content %}
       <h1>Welcome to My Site</h1>
       <p>This is the home page.</p>
   {% endblock %}
   ```

4. **Template Tags and Filters:**
   Django provides a range of built-in template tags and filters for performing logic, looping, and formatting data in templates. For example, the `for` tag is used for looping through lists, and the `date` filter is used for formatting dates. Here's an example:

   ```html
   <ul>
   {% for item in items %}
       <li>{{ item }}</li>
   {% endfor %}
   </ul>

   <p>Today's date: {{ today|date:"F j, Y" }}</p>
   ```

These are some fundamental aspects of working with Django templates in Python. They allow you to create dynamic web pages by combining HTML structure with Python logic.