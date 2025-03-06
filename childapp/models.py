from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Child(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    # Core fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    place = models.CharField(max_length=100, null=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    hobbies = models.TextField(blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    interests = models.TextField(blank=True)
    
    # Relationships
    guardian = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='guardian_children'
    )
    assigned_trainer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='trainer_children'
    )
    assigned_health_professional = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='health_professional_children'
    )

    # Additional fields for child management
    emergency_contact = models.CharField(max_length=100, default='Unknown', null=True)
    
    medical_conditions = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    school_name = models.CharField(max_length=100, blank=True)
    grade_level = models.CharField(max_length=20, blank=True)
    profile_photo = models.ImageField(upload_to='child_photos/', null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True, null=True)

    class Meta:
        verbose_name_plural = "Children"
        

    

    def age(self):
        from datetime import date
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

    