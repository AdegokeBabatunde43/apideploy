from django.db import models


# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    quantity=models.IntegerField()
    imageUrl1=models.URLField(blank=True)
    imageUrl2=models.URLField(blank=True)
    imageUrl3=models.URLField(blank=True)
    imageUrl4=models.URLField(blank=True)
    imageUrl5=models.URLField(blank=True)
    status=models.BooleanField(blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name