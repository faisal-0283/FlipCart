from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomerSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'customer'
        if commit:
            user.save()
        return user

class SellerSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'seller'
        if commit:
            user.save()
        return user


# accounts/forms.py

from django import forms

from django.contrib.auth.forms import AuthenticationForm

class CustomerLoginForm(AuthenticationForm):
    username = forms.CharField(label="Email / Username", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class SellerLoginForm(AuthenticationForm):
    username = forms.CharField(label="Seller Email / Username", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
