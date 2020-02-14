from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.TextField()
    usermail = models.TextField()
    password = models.TextField()
