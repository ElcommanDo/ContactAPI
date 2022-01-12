from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=220)
    last_name = models.CharField(max_length=220)
    phone_number = models.CharField(max_length=30)
    picture_url = models.URLField(null=True)
    is_favourite = models.BooleanField(default=True)



