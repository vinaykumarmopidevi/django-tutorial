from django.db import models
from django.urls import reverse

# Create your models here.
class Topic(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    
    def get_absolute_url(self):
        return reverse("create_view")
    
    
    def __str__(self):
        return self.title
