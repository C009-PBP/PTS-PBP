from django.db import models

from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class User(AbstractUser):
    is_pasien = models.BooleanField(default=False)
    is_dokter = models.BooleanField(default=False)

# class Pasien(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
#     user.is_pasien = True

# class Dokter(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
#     user.is_dokter = True

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.is_pasien:
#             Pasien.objects.create(user=instance)
#         elif instance.is_dokter:
#             Dokter.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.is_pasien:
#         instance.pasien.save()
#     elif instance.is_dokter:
#         instance.dokter.save()