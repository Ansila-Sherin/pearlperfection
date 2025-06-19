from django.db import models

# Create your models here.
class productTable(models.Model):
    product_name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    qty=models.IntegerField()
    price=models.IntegerField()
    image=models.ImageField(upload_to="profile")
class categorytable(models.Model):
    category_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    image=models.ImageField(upload_to="profile")