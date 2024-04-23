import django_filters
from .models import Book
from django import forms
class BookFilter(django_filters.FilterSet):
    price=django_filters.RangeFilter()
    genre=django_filters.MultipleChoiceFilter(Choices=Book.GenreChoices.choices,
                                            widget=forms.CheckboxSelectMultiple()
                                            )
    class Meta:
        model=Book
        #fields=['name','author__name','price','genre']
        fields={
        'name':['icontains'] ,
        'author__name':['icontains'],
        #'price':['lt','gt'],
        #'genre':['exact']
        }

