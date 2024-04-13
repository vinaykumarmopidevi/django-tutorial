from django.contrib import admin
from .models import Product
from .models import User
from .models import Department
from .models import Employee
from .models import Reporter
from .models import Article
from .models import Table1
from .models import Table2

# Register your models here.
admin.site.register(Product)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Table1)
admin.site.register(Table2)