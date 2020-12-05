from django import forms
from .models import Contact, Intro, About
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),

        }


class IntroForm(forms.ModelForm):
    class Meta:
        model = Intro
        fields = '__all__'

        widgets = {
            'interests': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'List 3 to 5 interests'}),
            'bio_message': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Brief description about yourself'}),

        }


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Height in inches'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City,State'}),
        }
