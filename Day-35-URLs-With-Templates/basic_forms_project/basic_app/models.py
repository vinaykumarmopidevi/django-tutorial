from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    
    
    def get_absolute_url(self):
        return reverse("basic_app:product_details", kwargs={"pk": self.pk})
    