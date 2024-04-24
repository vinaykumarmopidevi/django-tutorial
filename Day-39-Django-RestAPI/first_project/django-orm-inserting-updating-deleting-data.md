# Django ORM – Inserting, Updating & Deleting Data

```sh
python manage.py shell
from first_app.models import Song, Album
```

## Django ORM Queries

***Insert Data with Django ORM***

```python
a = Album(title = "Divide", artist = "Ed Sheeran", genre = "Pop")
a.save()

s = Song(name = "Castle on the Hill", album = a)
s.save()

a = Album(title = "Abbey Road", artist = "The Beatles", genre = "Rock")
a.save()

a = Album(title = "Revolver", artist = "The Beatles", genre = "Rock")
a.save()
```

***Retrieving Data with Django ORM***

```python
Album.objects.all()
Album.objects.filter(artist = "The Beatles")
Album.objects.exclude(genre = "Rock")
Album.objects.get(pk = 3)
Song.objects.select_related()  
```

***Update Data with Django ORM***

```python
a = Album.objects.get(pk = 3)
a.genre = "Pop"
a.save()
```

***Deleting Data with Django ORM***

```python
a = Album.objects.get(pk = 2)
a.delete()
Album.objects.all()

Album.objects.filter(genre = "Pop").delete()
Album.objects.all()
```
