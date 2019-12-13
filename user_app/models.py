from django.db import models

# Create your models here.


class UserModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    reputation = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

