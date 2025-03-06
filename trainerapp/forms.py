# forms.py (trainerapp/forms.py)
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Trainer

class TrainerCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=15)
    specialization = forms.CharField(max_length=100)
    experience = forms.IntegerField()
   
    fname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': ''
    }))
    lname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': ''
    }))

    class Meta:
        model = Trainer
        fields = ['phone', 'specialization', 'experience']  # Remove 'user' from here
        
    def save(self, commit=True):
        # Create User instance
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        
        # Create Trainer instance
        trainer = super().save(commit=False)
        trainer.user = user
        if commit:
            trainer.save()
        return trainer