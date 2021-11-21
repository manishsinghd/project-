from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=220)
    weight = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True, blank=True)
   

    def __str__(self):
        return self.name