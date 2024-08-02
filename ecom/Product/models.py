from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50,default="product")


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    size = models.IntegerField()

class Image(models.Model):
    variation = models.ForeignKey(Variation,  on_delete=models.CASCADE)
    product_image = models.FileField( upload_to=None, max_length=100)



