python .\manage.py load_bands
python .\manage.py shell   

q=Band.objects.all()
print(q.query)
SELECT "first_app_band"."id", "first_app_band"."name", "first_app_band"."genre" FROM "first_app_band"

from first_app.models import Band 
from django.db.models import Q

for e in Band.objects.all():
    print(e.genre)
for e in Band.objects.all():
    print(f"{e.name} --- {e.genre}")	
	
Band.objects.all().values()

Band.objects.values_list('genre',flat=True)
Band.objects.values_list('genre',flat=True).distinct()

Band.objects.filter(genre='Post Punk').values()
SELECT * FROM Band WHERE genre = 'Post Punk';

Band.objects.filter(genre='Post Punk').values().count()
SELECT count(*) FROM first_app_band WHERE genre = 'Post Punk';

Band.objects.filter(name= 'Gang of Four', id=16).values()
SELECT * FROM Band WHERE name= 'Gang of Four' AND id = 16;

Band.objects.filter(genre='Jazz').values() | Band.objects.filter(genre='Hip Hop').values()
SELECT * FROM Band WHERE genre='Jazz' OR genre='Hip Hop';

punk=Band.objects.filter(genre='Post Punk')
rock=Band.objects.filter(genre='Classic Rock')
pr=punk|rock 
print(pr.query)
SELECT "first_app_band"."id", "first_app_band"."name", "first_app_band"."genre" FROM "first_app_band" WHERE ("first_app_band"."genre" = Post Punk OR "first_app_band"."genre" = Classic Rock)

punlrock=punk.union(rock)
print(punlrock.query)
SELECT "first_app_band"."id" AS "col1", "first_app_band"."name" AS "col2", "first_app_band"."genre" AS "col3" FROM "first_app_band" WHERE "first_app_band"."genre" = Post Punk UNION SELECT "first_app_band"."id" AS "col1", "first_app_band"."name" AS "col2", "first_app_band"."genre" AS "col3" FROM "first_app_band" WHERE "first_app_band"."genre" = Classic Rock

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



Band.objects.filter(name__startswith='L').values(); 
SELECT * FROM Band WHERE name LIKE 'L%'

https://www.w3schools.com/django/django_queryset_filter.php

Band.objects.all().order_by('name').values()
for e in names:
    print(e['name'])

SELECT * FROM Band ORDER BY name DESC;

Band.objects.all().order_by('name', '-id').values()
SELECT * FROM members ORDER BY lastname ASC, id DESC;

