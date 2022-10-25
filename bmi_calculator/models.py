from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BMI(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    jenis_kelamin = models.TextField()
    umur = models.BigIntegerField()
    tinggi = models.BigIntegerField()
    berat = models.BigIntegerField()
    date_created = models.DateField()
