from django.core.management.base import BaseCommand
from myapp.models import Book,Author

class Command(BaseCommand):
    help = 'Load book data'
    
    def handle(self, *args, **kwargs):
        #create author
        orwell=Author.objects.get_or_create(name="George Orwell")[0]
        jong=Author.objects.get_or_create(name="Erica Jong")[0]
        sobol=Author.objects.get_or_create(name="Donald J. Sobol")[0]
        kalanithi=Author.objects.get_or_create(name="Paul Kalanithi")[0]
        twain=Author.objects.get_or_create(name="Mark Twain")[0]
        philbrick=Author.objects.get_or_create(name="Nathaniel Philbrick")[0]
        alcott=Author.objects.get_or_create(name="Louisa May Alcott")[0]
        white=Author.objects.get_or_create(name="E. B. White")[0]
        juster=Author.objects.get_or_create(name="Norton Juster")[0]
        greene=Author.objects.get_or_create(name="Graham Greene")[0]
        
        #create books
        # This line of code is creating a new `Book` object in the database if it doesn't already
        # exist. It is using the `get_or_create` method provided by Django's ORM (Object-Relational
        # Mapping) to either retrieve an existing `Book` object with the specified attributes or
        # create a new one if it doesn't exist.
        Book.objects.get_or_create(
            name='Jane Eyre',
            author=orwell,
            price=10.99,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=4
            
        )
        Book.objects.get_or_create(
            name='Fear of Flying',
            author=jong,
            price=34.45,
            genre=Book.GenreChoices.CRIME,
            number_in_stock=40
            
        )
        Book.objects.get_or_create(
            name='Encyclopedia Brown, Boy Detective',
            author=sobol,
            price=47.45,
            genre=Book.GenreChoices.NON_FICTION,
            number_in_stock=23
            
        )
        Book.objects.get_or_create(
            name='When Breath Becomes Air',
            author=kalanithi,
            price=10.45,
            genre=Book.GenreChoices.OTHER,
            number_in_stock=12
            
        )
        Book.objects.get_or_create(
            name='The Adventures of Tom Sawyer',
            author=twain,
            price=20.90,
            genre=Book.GenreChoices.NON_FICTION,
            number_in_stock=15
            
        )
        Book.objects.get_or_create(
            name='In the Heart of the Sea',
            author=philbrick,
            price=56.90,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=56
            
        )
        Book.objects.get_or_create(
            name='Little Women',
            author=alcott,
            price=16.90,
            genre=Book.GenreChoices.OTHER,
            number_in_stock=34
            
        )
        Book.objects.get_or_create(
            name='Charlotte’s Web',
            author=white,
            price=57.90,
            genre=Book.GenreChoices.CRIME,
            number_in_stock=12
            
        )
        Book.objects.get_or_create(
            name='The Heart of the Matterh',
            author=juster,
            price=78.25,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=61
            
        )
        Book.objects.get_or_create(
            name='The Phantom Tollbooth',
            author=greene,
            price=98.25,
            genre=Book.GenreChoices.CRIME,
            number_in_stock=47
            
        )