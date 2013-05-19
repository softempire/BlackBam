from django.db import models

# Create your models here.

class Contact(models.Model):
    subject = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    message = models.CharField(max_length=10)