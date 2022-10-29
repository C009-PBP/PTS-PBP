from email.policy import default
from django.db import models
from authentication.models import User

# Create your models here.
class InfoDokter(models.Model):
    nama_dokter = models.TextField(default='')
    hari_praktek = models.TextField(default='')
    jadwal_praktek = models.TextField()
    

class ReviewDokter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(default='')