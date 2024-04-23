# Query Set Operations

```sh
python .\manage.py load_bands
python .\manage.py shell   
```

```python
q=Band.objects.all()
print(q.query)
```

```sql
SELECT "first_app_band"."id", "first_app_band"."name", "first_app_band"."genre" FROM "first_app_band"
```

```python
from first_app.models import Band 
from django.db.models import Q
```

```python
for e in Band.objects.all():
    print(e.genre)
```

```python
Band.objects.all().values()

Band.objects.values_list('genre',flat=True)
Band.objects.values_list('genre',flat=True).distinct()

Band.objects.filter(genre='Post Punk').values()
```

```sql
SELECT * FROM Band WHERE genre = 'Post Punk';
```

```python
Band.objects.filter(genre='Post Punk').values().count()
```

```sql
SELECT count(*) FROM first_app_band WHERE genre = 'Post Punk';
```

```python
Band.objects.filter(name= 'Gang of Four', id=16).values()
```

```sql
SELECT * FROM Band WHERE name= 'Gang of Four' AND id = 16;
```

```python
Band.objects.filter(genre='Jazz').values() | Band.objects.filter(genre='Hip Hop').values()
```

```sql
SELECT * FROM Band WHERE genre='Jazz' OR genre='Hip Hop';
```

```python
punk=Band.objects.filter(genre='Post Punk')
rock=Band.objects.filter(genre='Classic Rock')
pr=punk|rock 
print(pr.query)
```

```sql
SELECT "first_app_band"."id", "first_app_band"."name", "first_app_band"."genre" FROM "first_app_band" WHERE ("first_app_band"."genre" = Post Punk OR "first_app_band"."genre" = Classic Rock)
```

```python
punlrock=punk.union(rock)
print(punlrock.query)
```

```sql
SELECT "first_app_band"."id" AS "col1", "first_app_band"."name" AS "col2", "first_app_band"."genre" AS "col3" FROM "first_app_band" WHERE "first_app_band"."genre" = Post Punk UNION SELECT "first_app_band"."id" AS "col1", "first_app_band"."name" AS "col2", "first_app_band"."genre" AS "col3" FROM "first_app_band" WHERE "first_app_band"."genre" = Classic Rock
```

```python

from django.db.models import Q
punk_q=Q(genre="Punk")
rock_q=Q(genre="Classic Rock")
Band.objects.filter(punk_q|rock_q)


for i in Band.objects.filter(punk_q|rock_q).values_list('name'):
    print(i)

Band.objects.filter(name__iregex=r"^[a-d].*$").values_list('name')

for e in Band.objects.filter(name__iregex=r"^[a-d].*$").values_list('name'):
    print(e[0])

for e in Band.objects.filter(name__iregex=r"^[a-d].*$").values_list().values_list() :
    print(e)
	
punk=Band.objects.filter(genre='Punk') 	
band_ad=Band.objects.filter(name__iregex=r"^[a-d].*$")     
bands_ad.intersection(punk)
punk_ad=bands_ad.intersection(punk) 
punk_ad.values_list()
print(punk_ad.query)

band_ad & punk

band_ad.filter(genre="Punk")
Band.objects.filter(name__iregex=r"^[a-d].*$",genre='Punk')    

band_ad.union(punk,all=True)

band_ad.difference(punk) 
band_ad.exclude(genre='Punk') 
startwith=Q(name__iregex=r"^[aeiou].*$") 
jazz_hiphop=Q(genre__in=['Jazz','Hip Hop'])  
Band.objects.filter(startwith & jazz_hiphop)
Band.objects.filter(startwith | jazz_hiphop)

```

```python
Band.objects.filter(name__startswith='L').values(); 
```

```sql
SELECT * FROM Band WHERE name LIKE 'L%'
```

[django queryset filter](https://www.w3schools.com/django/django_queryset_filter.php)

```python
Band.objects.all().order_by('name').values()
for e in names:
    print(e['name'])
```

```sql
SELECT * FROM Band ORDER BY name DESC;
```

```python
Band.objects.all().order_by('name', '-id').values()
```

```sql
SELECT * FROM members ORDER BY lastname ASC, id DESC;
```



Method that returns queryset
1.filter()

question.objects.filter(id=1)
2.exclude()

Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3), headline='Hello')
3.annotate()

 q = Blog.objects.annotate(number_of_entries=Count('entry'))
4.order_by()

Entry.objects.filter(pub_date__year=2005).order_by('-pub_date', 'headline')
Entry.objects.order_by('?')             #order randomly
Entry.objects.order_by('blog__id')
Entry.objects.order_by(Coalesce('summary', 'headline').desc())
5.reverse()

my_queryset.reverse()[:5]
6.distinct()

Entry.objects.order_by('author', 'pub_date').distinct('author')
7.values()

Blog.objects.filter(name__startswith='Beatles').values()
8.values_list()

>>>Entry.objects.values_list('id', 'headline')
<QuerySet [(1, 'First entry'), ...]>
9.dates()

10.datetimes()

11.none()

Entry.objects.none()
12.union()

qs1 = Author.objects.values_list('name')
qs2 = Entry.objects.values_list('headline')
qs1.union(qs2).order_by('name')
13.intersection()

>>> qs1.intersection(qs2, qs3)
14.difference()

>>> qs1.difference(qs2, qs3)
15.extra()

select
where / tables
order_by
params
16.defer()

Entry.objects.defer("body").filter(rating=5).defer("headline")
17.only()

Opposite of defer()
Person.objects.defer("age", "biography")
Person.objects.only("name")
18.using()

Entry.objects.using('backup')
19.select_for_update()

Method that does not return queryset
get()
Because it returns a python object form, not a queryset, it can be accessed using dot nation.
User.objects.get(id=1).name
create()

get_or_create()

Returns a tuple (object, created).
obj, created = Person.objects.get_or_create(
    first_name='John',
    last_name='Lennon',
    defaults={'birthday': date(1940, 10, 9)},
)
update_or_create

count()

6.iterator()

7.latest()

8.earliest()

9.first()

10.last()

11.aggregate()

q = Blog.objects.aggregate(number_of_entries=Count('entry'))
12.exists()

13.update()

14.delete()

15.explain()

Field lookups
Used when specifying the WHERE statement of SQL.
1.extact

Entry.objects.get(id__exact=14)
Entry.objects.get(id__exact=None)

SELECT ... WHERE id = 14;
SELECT ... WHERE id IS NULL;
2.iexact

#'Beatles Blog', 'beatles blog', 'BeAtLes BLoG 와 매치된다.
Blog.objects.get(name__iexact='beatles blog')  

Blog.objects.get(name__iexact=None)

SELECT ... WHERE name ILIKE 'beatles blog';
SELECT ... WHERE name IS NULL;
3.contains

Entry.objects.get(headline__contains='Lennon')

SELECT ... WHERE headline LIKE '%Lennon%';
4.icontains

Entry.objects.get(headline__icontains='Lennon')

SELECT ... WHERE headline ILIKE '%Lennon%';
5.in

inner_qs = Blog.objects.filter(name__contains='Cheddar')
entries = Entry.objects.filter(blog__in=inner_qs)

SELECT ... WHERE blog.id IN (SELECT id FROM ... WHERE NAME LIKE '%Cheddar%')
6.gt(greater than)

Entry.objects.filter(id__gt=4)
7.gte(greater than equal)

8.lt(less than)

9.lte(less than equal)

10.startswith

Entry.objects.filter(headline__startswith='Lennon')
11.istartswith

Entry.objects.filter(headline__istartswith='Lennon')
12.endswith

Entry.objects.filter(headline__endswith='Lennon')
13.iendswith

Entry.objects.filter(headline__iendswith='Lennon')
14.range

import datetime
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date(2005, 3, 31)
Entry.objects.filter(pub_date__range=(start_date, end_date))
15.date / year /month / day / week / week_day

Entry.objects.filter(pub_date__date=datetime.date(2005, 1, 1))
Entry.objects.filter(pub_date__date__gt=datetime.date(2005, 1, 1))

Entry.objects.filter(pub_date__year=2005)
Entry.objects.filter(pub_date__year__gte=2005)

Entry.objects.filter(pub_date__month=12)
Entry.objects.filter(pub_date__month__gte=6)

Entry.objects.filter(pub_date__day=3)
Entry.objects.filter(pub_date__day__gte=3)

Entry.objects.filter(pub_date__week=52)
Entry.objects.filter(pub_date__week__gte=32, pub_date__week__lte=38)

Entry.objects.filter(pub_date__week_day=2)
Entry.objects.filter(pub_date__week_day__gte=2)
Aggregation function
1.expressions

2.output_field

3.filter

4.Avg

5.Count

6.Max

7.Min

8.Sum



# Cheatsheet for Django QuerySets
Current Django Version: [1.11](https://docs.djangoproject.com/en/1.11/ref/models/querysets/)

## Methods that return new [QuerySets](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#methods-that-return-new-querysets)

**Can be chained:**

```python
Entry.objects.filter(**kwargs).exclude(**kwargs).order_by(**kwargs)
```

 * [filter](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#filter)
 ```python
 Entry.objects.filter(id__in=[1, 3, 4])
 SELECT ... WHERE id IN (1, 3, 4);
 
 inner_qs = Blog.objects.filter(name__contains='Cheddar')
 entries = Entry.objects.filter(blog__in=inner_qs)
 SELECT ... WHERE blog.id IN (SELECT id FROM ... WHERE NAME LIKE '%Cheddar%')
 ``` 
 
 * [exclude](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#exclude)
 ```python
 Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3), headline='Hello')
 SELECT ... WHERE NOT (pub_date > '2005-1-3' AND headline = 'Hello')
 
 Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3))/
 .exclude(headline='Hello')
 SELECT ... WHERE NOT pub_date > '2005-1-3' AND NOT headline = 'Hello'
 ```
 * [annotate](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#annotate)
 ```python
 >>> from django.db.models import Count
 >>> q = Blog.objects.annotate(Count('entry'))
 # The name of the first blog
 >>> q[0].name
 'Blogasaurus'
 # The number of entries on the first blog
 >>> q[0].entry__count
 42
 
 >>> q = Blog.objects.annotate(number_of_entries=Count('entry'))
 # The number of entries on the first blog, using the name provided
 >>> q[0].number_of_entries
 42
 ```
 * [order_by](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#order-by)
 ```python
 Entry.objects.filter(pub_date__year=2005).order_by('-pub_date', 'headline')
 The result above will be ordered by pub_date descending, 
 then by headline ascending. 
 The negative sign in front   of "-pub_date" indicates descending order. 
 Ascending order is implied. 
 
 # No Join
 Entry.objects.order_by('blog_id')
 # Join
 Entry.objects.order_by('blog__id')
 ```
 * [reverse](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#reverse)
 ```python
 Use the reverse() method to reverse the order in 
 which a queryset’s elements are returned. 
 Calling reverse() a second time restores the ordering back to the normal direction.
 
 my_queryset.reverse()[:5]
 ```
 * [distinct](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#distinct)
 ```python
 When using distinct() and values() together, be careful when ordering by fields
 not in the values() call.
 
 When you specify field names, you must provide an order_by() in the QuerySet, 
 and the fields in order_by() must  start with the fields in distinct(), 
 in the same order.
 
 Author.objects.distinct()

 Entry.objects.order_by('pub_date').distinct('pub_date')
 
 Entry.objects.order_by('blog__name', 'mod_date').distinct('blog__name', 'mod_date')
 ```
 * [values](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#values)
 ```python
 Blog.objects.filter(name__startswith='Beatles').values()
 [{'id': 1, 'name': 'Beatles Blog', 'tagline': 'All the latest Beatles news.'}]
 
 Entry.objects.values('blog_id')
 [{'blog_id': 1}, ...]
 
 Blog.objects.values('name', 'entry__headline')
 [{'name': 'My blog', 'entry__headline': 'An entry'},
     {'name': 'My blog', 'entry__headline': 'Another entry'}, ...]
 ```
 * [values_list](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#values-list)
 ```python
 Entry.objects.values_list('id', 'headline')
 [(1, 'First entry'), ...]
 
 Entry.objects.values_list('id', flat=True).order_by('id')
 [1, 2, 3, ...]
 ```
 * [dates](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#dates)
 ```python
 field should be the name of a DateField of your model. 
 kind should be either "year", "month" or "day". 
 Each datetime.date object in the result list is “truncated” to the given type.

 * "year" returns a list of all distinct year values for the field.
 * "month" returns a list of all distinct year/month values for the field.
 * "day" returns a list of all distinct year/month/day values for the field.
 
 Entry.objects.dates('pub_date', 'year')
 [datetime.date(2005, 1, 1)]
 
 Entry.objects.dates('pub_date', 'month')
 [datetime.date(2005, 2, 1), datetime.date(2005, 3, 1)]

 Entry.objects.dates('pub_date', 'day')
 [datetime.date(2005, 2, 20), datetime.date(2005, 3, 20)]

 Entry.objects.dates('pub_date', 'day', order='DESC')
 [datetime.date(2005, 3, 20), datetime.date(2005, 2, 20)]
 ```
 * [datetimes](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#datetimes)
 ```python
 tzinfo defines the time zone to which datetimes are converted prior to truncation. 
 Indeed, a given datetime has different representations depending on the time zone in use. 
 This parameter must be a datetime.tzinfo object. 
 If it’s None, Django uses the current time zone. It has no effect when USE_TZ is False.
 
 This function performs time zone conversions directly in the database. 
 As a consequence, your database must be able to interpret the value of tzinfo.tzname(None). 
 This translates into the following requirements:

 * SQLite: install pytz — conversions are actually performed in Python.
 * PostgreSQL: no requirements (see Time Zones).
 * Oracle: no requirements (see Choosing a Time Zone File).
 * MySQL: install pytz and load the time zone tables with mysql_tzinfo_to_sql.
 ```
 * [none](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#none)
 ```python
 Calling none() will create a queryset that never returns any objects and 
 no query will be executed when accessing the results. 
 A qs.none() queryset is an instance of EmptyQuerySet.
 
 Entry.objects.none()
 []
 
 from django.db.models.query import EmptyQuerySet
 isinstance(Entry.objects.none(), EmptyQuerySet)
 True
 ```
 * [all](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#all)
 ```python
 Returns a copy of the current QuerySet (or QuerySet subclass).
 When a QuerySet is evaluated, it typically caches its results. 
 If the data in the database might have changed since a QuerySet was evaluated, 
 you can get updated results for the same query by calling all() 
 on a previously evaluated QuerySet.
 ```
 * [select_related](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#select-related)
 ```python
 e = Entry.objects.get(id=5) # Hits the database.
 b = e.blog # Hits the database again to get the related Blog object.
 
 # Hits the database.
 e = Entry.objects.select_related('blog').get(id=5)

 # Doesn't hit the database, because e.blog has been prepopulated
 # in the previous query.
 b = e.blog
 
 b = Book.objects.select_related('author__hometown').get(id=4)
 p = b.author         # Doesn't hit the database.
 c = p.hometown       # Doesn't hit the database.

 b = Book.objects.get(id=4) # No select_related() in this example.
 p = b.author         # Hits the database.
 c = p.hometown       # Hits the database.
 ```