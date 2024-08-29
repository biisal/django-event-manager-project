# forms.py

from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'w-full p-2 bg-[#232323aa] outline-none rounded mt-8', 'placeholder': 'Email', 'required': True})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'bg-transparent outline-none', 'placeholder': 'Password', 'id': 'password', 'required': True})
    )

class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w-full p-2 bg-[#232323aa] outline-none rounded mt-8', 'placeholder': 'Username', 'required': True})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'w-full p-2 bg-[#232323aa] outline-none rounded mt-4', 'placeholder': 'Email', 'required': True})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'bg-transparent outline-none', 'placeholder': 'Password', 'id': 'password', 'required': True})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'bg-transparent outline-none', 'placeholder': 'Confirm Password', 'id': 'confirm_password', 'required': True})
    )