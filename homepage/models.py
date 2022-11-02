<<<<<<< HEAD
=======
from email.policy import default
>>>>>>> cb11860 (fixed bootstrap ver)
from django.db import models
from authentication.models import User
# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, db_constraint=False, null=True, blank=True)
    date_created = models.DateField()
    review = models.TextField()
    username = models.TextField(default="")