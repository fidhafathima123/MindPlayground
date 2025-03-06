from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HealthPro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
      
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    specialization = models.CharField(max_length=255,blank=True,null=True)
    date_joined = models.DateField(auto_now_add=True)
    certification = models.FileField(upload_to='certifications/',blank=True,null=True)

    def __str__(self):
        return f"{self.user.username} "
    
    