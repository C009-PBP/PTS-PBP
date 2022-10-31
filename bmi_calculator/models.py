from django.db import models
# from django.contrib.auth.models import User
# from authentication.models import User, Pasien
from authentication.models import User
# Create your models here.
class BMI(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, db_constraint=False)
    umur = models.BigIntegerField()
    tinggi = models.BigIntegerField()
    berat = models.BigIntegerField()
    date_created = models.DateField()
    bmi_result = models.BigIntegerField()
    deskripsi_hasil = models.TextField(default="Belum diketahui")
    keterangan_tambahan = models.TextField(default="Perhitungan BMI ini ditujukan untuk orang dewasa berusia lebih dari 19 tahun. Karena faktor pertumbuhan yang terus menerus terjadi secara cepat, perhitungan BMI bagi orang berusia di bawah 19 tahun akan berdasar pada relativitas hasil BMI terhadap populasi dengan umur yang sama.")

