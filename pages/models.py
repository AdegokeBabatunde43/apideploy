from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone= models.IntegerField()
    date= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
    



class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    