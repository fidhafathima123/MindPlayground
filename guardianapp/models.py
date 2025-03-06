from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Guardian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
   
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    occupation = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    relation_to_child = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.relation_to_child}"