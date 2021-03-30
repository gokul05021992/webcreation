from django.db import models

class employee(models.Model):
    id =models.CharField(primary_key=True)
    name=models.CharField(max_length=50)


# Create your models here.
