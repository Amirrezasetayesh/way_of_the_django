from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    # UserCreationForm is import to views.py
    #label == write somthing upside of your parameter
    #widget give some attrs like(class , name , place holder ) and name is the name of your parameter and placeholder some word in yor textbox
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


    # if you want your class (from class) do somthing , you should make one Meta class
    class Meta:
        # at the first you need one user model to use you form
        model = User
        # you should set all  parameters of you form to some field and the order of this fields is order of how person can see your parameters
        fields = ( 'email', 'username', 'password1', 'password2')