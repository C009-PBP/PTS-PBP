from django.db import models

from authentication.models import User
# Create your models here.
class Forum(models.Model):
    question_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False, auto_now_add=True)
    specialization = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    question_text = models.TextField(blank=True, null=True)
    is_answered = models.BooleanField(default=False)
