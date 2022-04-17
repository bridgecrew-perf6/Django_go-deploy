from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
# Create your models here.
class customer(models.Model):
    username=models.OneToOneField(User,null=True, on_delete=models.CASCADE, blank=True)
    Name=models.CharField(max_length=150, null=True)
    contactno=models.CharField(max_length=150, null=True)
    email=models.CharField(max_length=150, null=True)
    
    def __str__(self): #display name istead of id
        return str(self.Name)

