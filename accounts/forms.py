from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# -----------------------------
# Customer Sign Up Form
# -----------------------------
class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "placeholder": "Enter your email",
            "class": "form-control"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={
                "placeholder": "Enter username",
                "class": "form-control"
            }),
            "password1": forms.PasswordInput(attrs={
                "placeholder": "Enter password",
                "class": "form-control"
            }),
            "password2": forms.PasswordInput(attrs={
                "placeholder": "Confirm password",
                "class": "form-control"
            }),
        }


# -----------------------------
# Seller Sign Up Form
# -----------------------------
class SellerSignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "placeholder": "Enter your email",
            "class": "form-control"
        })
    )

    shop_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter your shop name",
            "class": "form-control"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={
                "placeholder": "Enter username",
                "class": "form-control"
            }),
            "password1": forms.PasswordInput(attrs={
                "placeholder": "Enter password",
                "class": "form-control"
            }),
            "password2": forms.PasswordInput(attrs={
                "placeholder": "Confirm password",
                "class": "form-control"
            }),
        }


# -----------------------------
# Customer Login Form
# -----------------------------
class CustomerLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter username",
        "class": "form-control"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password",
        "class": "form-control"
    }))


# -----------------------------
# Seller Login Form
# -----------------------------
class SellerLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter seller username",
        "class": "form-control"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password",
        "class": "form-control"
    }))
