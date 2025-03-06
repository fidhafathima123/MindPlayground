from django import forms
from .models import Guardian
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class GuardianRegistrationForm(forms.ModelForm):
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
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': ''
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': ''
    }))
    address = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': '',
        'rows': 3
    }))
    occupation = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': ''
    }))
    place = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': ''
    }))
    relation_to_child = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': ''
    }))

    class Meta:
        model = Guardian
        fields = ['username','password','fname', 'lname', 'phone', 'email', 'address', 'occupation', 'place', 'relation_to_child']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['fname'],
            last_name=self.cleaned_data['lname']
        )
        guardian = super().save(commit=False)
        guardian.user = user
        if commit:
            guardian.save()
        return guardian
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if User.objects.filter(username=username).exists():
            self.add_error('username', 'This username is already taken.')

        if User.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already registered.')

        return cleaned_data