from django import forms
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError
from .models import Product

def check_first_char_m(value):
    if value[0].lower() != 'm':
        raise forms.ValidationError("name should start with char m")

class FormName(forms.Form):
    name=forms.CharField()

    def clean(self):
        all_clean_data = super().clean()
        name=all_clean_data['name']

        if name != 'vinay':
            raise ValidationError(f'name error {name}')
        
class ProductForm(forms.ModelForm):
    
    class Meta:
        model=Product
        fields=['name','description','price']
