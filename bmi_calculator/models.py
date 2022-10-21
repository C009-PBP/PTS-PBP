from django.db import models

# Create your models here.
class BMI(models.Model):
    height = models.BigIntegerField()
    weight = models.BigIntegerField()
    age = models.BigIntegerField()
    