from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    number=models.CharField(max_length=10)
    content=models.TextField(max_length=500)