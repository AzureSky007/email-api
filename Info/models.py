from django.db import models

# Create your models here.
class User(models.Model):
    num = models.CharField(max_length=20, primary_key= True)
    greet = models.CharField(max_length= 50, null = True)
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    
    