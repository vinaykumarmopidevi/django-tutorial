# forms

In Django, forms are a fundamental part of building web applications, especially when it comes to collecting and validating user input. Django provides a convenient way to define and handle forms using its built-in `forms` module. Here's a basic overview of how to work with forms in Django:

1. **Creating a Form Class**: You define your forms using a Python class that subclasses `django.forms.Form` or `django.forms.ModelForm` depending on whether you're working with regular forms or forms tied to models. You specify the fields of the form as class attributes.

   ```python
   from django import forms

   class MyForm(forms.Form):
       name = forms.CharField(max_length=100)
       email = forms.EmailField()
       message = forms.CharField(widget=forms.Textarea)
   ```

2. **Rendering Forms in Templates**: You can render forms in your templates using the `{{ form }}` template tag. Django will automatically generate the HTML for the form fields based on the form class you defined.

   ```html
   <form method="post">
       {% csrf_token %}
       {{ form.as_p }}
       <button type="submit">Submit</button>
   </form>
   ```

3. **Handling Form Submission**: In your view function, you handle form submission by checking the request method. If it's a POST request, you instantiate the form with the submitted data, validate it, and then process the data if it's valid.

   ```python
   from django.shortcuts import render, redirect
   from .forms import MyForm

   def my_view(request):
       if request.method == 'POST':
           form = MyForm(request.POST)
           if form.is_valid():
               # Process the form data
               name = form.cleaned_data['name']
               email = form.cleaned_data['email']
               message = form.cleaned_data['message']
               # Do something with the data
               return redirect('success_url')
       else:
           form = MyForm()
       return render(request, 'my_template.html', {'form': form})
   ```

4. **Form Validation**: Django's form system automatically performs validation according to the field types and options you specify in the form class. You can also define custom validation logic by adding methods to your form class whose names start with `clean_`.

   ```python
   class MyForm(forms.Form):
       # Field definitions

       def clean_name(self):
           name = self.cleaned_data['name']
           # Custom validation logic
           if len(name) < 3:
               raise forms.ValidationError("Name must be at least 3 characters long.")
           return name
   ```

5. **Using ModelForm**: If you're working with models, you can use `ModelForm` to automatically create a form based on a model.

   ```python
   from django import forms
   from .models import MyModel

   class MyModelForm(forms.ModelForm):
       class Meta:
           model = MyModel
           fields = ['field1', 'field2']  # Specify which fields to include in the form
   ```

This is just a basic overview of working with forms in Django. There's a lot more you can do, including handling file uploads, customizing form rendering, and using form sets for working with multiple forms on the same page.