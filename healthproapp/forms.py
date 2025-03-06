from django import forms
from .models import HealthPro
from django.contrib.auth.models import User

class HealthproCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password'
    }))
    fname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': ''
    }))
    lname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': ''
    }))
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=15)
    
    class Meta:
        model = HealthPro
        fields = ['place', 'phone',]
        widgets = {
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'certification': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    def save(self, commit=True):
          
        # Create User instance
        user = User.objects.create_user(
          username=self.cleaned_data['username'],
          email=self.cleaned_data['email'],
          password=self.cleaned_data['password']
        )
        
        # Create HealthProfessional instance
        health_pro = super().save(commit=False)
        health_pro.user = user
        if commit:
            health_pro.save()
        return health_pro