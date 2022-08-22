from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    user_type_data = ((1,'ADMIN'),(2,'STAFF'),(3,'STUDENT'))
    user_type = models.CharField(default = 1,max_length=10, choices=user_type_data)
