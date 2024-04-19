from django.shortcuts import render
from .models import Book
from .filters import BookFilter

# Create your views here.
def index(request):
    """
    name=request.GET.get("name")
    books=Book.objects.all()
    if name:
        books=books.filter(name__icontains=name)
    
    context={
        "form":BookNameFilterForm,
        "books":books
        
        
    }
    """
    book_filter=BookFilter(request.GET,queryset=Book.objects.all())
    context={
        'form':book_filter.form,
        'books':book_filter.qs
    }
    
    return render(request,"index.html",context=context)
