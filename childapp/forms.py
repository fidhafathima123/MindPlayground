from django import forms
from .models import Child
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class ChildRegistrationForm(forms.ModelForm):
    fname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': ''
    }))
    lname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': ''
    }))
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': ''
    }))
    
    # Custom validators
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    # Additional fields for validation
    
    class Meta:
        model = Child
        fields = [
            
            'place',
            'phone',
            'hobbies',
            'date_of_birth',
            'gender',
            'interests',
            'emergency_contact',
            
            'medical_conditions',
            'allergies',
            'school_name',
            'grade_level',
            'profile_photo'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            
            'place': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': ' location'}
            ),
            'phone': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': ' phone number'}
            ),
            'hobbies': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': ' hobbies'}
            ),
            'interests': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': ' interests'}
            ),
            'medical_conditions': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': ' any medical conditions'}
            ),
            'allergies': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': ' any allergies'}
            ),
            'gender': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'emergency_contact': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': ' emergency contact name'}
            ),
            
            'school_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': ' school name'}
            ),
            'grade_level': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': ' grade level'}
            ),
            'profile_photo': forms.FileInput(
                attrs={'class': 'form-control'}
            ),
        }
    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['fname'],
            last_name=self.cleaned_data['lname']
        )
        child = super().save(commit=False)
        child.user = user
        if commit:
            child.save()
        return child
    def clean(self):
        cleaned_data = super().clean()
        # Validate emergency phone numbers match
        
        

        # Validate date of birth is not in the future
        dob = cleaned_data.get('date_of_birth')
        if dob:
            from datetime import date
            if dob > date.today():
                raise forms.ValidationError("Date of birth cannot be in the future.")

        return cleaned_data

    def clean_profile_photo(self):
        photo = self.cleaned_data.get('profile_photo')
        if photo:
            # Validate file size (max 5MB)
            if photo.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Profile photo must be no larger than 5MB")
            # Validate file type
            import os
            ext = os.path.splitext(photo.name)[1]
            valid_extensions = ['.jpg', '.jpeg', '.png']
            if not ext.lower() in valid_extensions:
                raise forms.ValidationError("Please upload a valid image file (jpg, jpeg, png)")
        return photo

class ChildUpdateForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = [
            
            'place',
            'phone',
            'hobbies',
            'interests',
            'emergency_contact',
            
            'medical_conditions',
            'allergies',
            'school_name',
            'grade_level',
            'profile_photo'
        ]
        widgets = {
            # Same widget definitions as ChildRegistrationForm
            
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'hobbies': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'interests': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control'}),

            'medical_conditions': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'allergies': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'school_name': forms.TextInput(attrs={'class': 'form-control'}),
            'grade_level': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }