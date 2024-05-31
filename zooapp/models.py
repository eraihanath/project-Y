from email.message import Message
from django.db import models


# Create your models here.

class Contact(models.Model):
    Name    = models.CharField(max_length=30)
    Email   = models.EmailField(max_length=25)
    Subject = models.CharField(max_length=34)
    Message = models.TextField()
    Date    = models.CharField(default='DD-MM-YYYY',max_length=12)



