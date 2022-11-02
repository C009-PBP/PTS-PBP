from django.db import models
from authentication.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='images/profile')
    birth_date = models.DateField(max_length=8, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)

    emergency_firstname = models.CharField(max_length=255, blank=True, null=True)
    emergency_lastname = models.CharField(max_length=255, blank=True, null=True)
    emergency_relationship = models.CharField(max_length=255, blank=True, null=True)
    emergency_phone_no = models.CharField(max_length=20, blank=True, null=True)
    emergency_street = models.CharField(max_length=255, blank=True, null=True)
    emergency_city = models.CharField(max_length=255, blank=True, null=True)
    emergency_province = models.CharField(max_length=255, blank=True, null=True)

    bloodtype = models.CharField(max_length=255, blank=True, null=True)
    bloodpressure = models.CharField(max_length=255, blank=True, null=True)
    illnesses = models.CharField(max_length=255, blank=True, null=True)
    allergies = models.CharField(max_length=255, blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()