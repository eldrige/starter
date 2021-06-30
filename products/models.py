from django.db import models

# Create your models here.
# blank = false, means the field is required, null refers to the val in the db


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField()
