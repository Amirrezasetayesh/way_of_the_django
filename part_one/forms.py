from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    # UserCreationForm is import to views.py
    email = forms.EmailField(
        label="your email:",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )

    username = forms.CharField(
        label="you username:",
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )

    password1 = forms.CharField(
        label="you password:",
        widget=forms.PasswordInput(attrs={'class':'form-control',
                                          'name':'password',
                                          'type':'password',
                                          'placeholder':'password'

        })
    )
    password2 = forms.CharField(
        label="you password:",
        widget=forms.PasswordInput(attrs={'class':'form-control',
                                          'name':'password',
                                          'type':'password',
                                          'placeholder':'write again'

        })
    )



    class Meta:
        model = User
        fields = ( 'email', 'username', 'password1', 'password2')