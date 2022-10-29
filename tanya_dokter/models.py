from django.db import models
# from django.conf import settings
from authentication.models import User
# from django.db.models.fields import DateTimeField
# from django.http.response import HttpResponseRedirect
# from django.utils.timezone import now


# Create your models here.
class Forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False, auto_now_add=True)
    specialization = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    question = models.TextField()

    def __str__(self):
        return str(self.title)


# class Comment(models.Model):
#     post = models.ForeignKey(Forum, related_name="comments",
#                               on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL)
#     reply = models.TextField()
#     repDate = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.post.title) + " " + str(self.user)
