from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models.Customer import Customer

class CustomUserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CustomUserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs["class"] = 'form-control'
        self.fields['username'].widget.attrs["placeholder"] = 'Your Username ...'
        self.fields['email'].widget.attrs["class"] = 'form-control'
        self.fields['email'].widget.attrs["placeholder"] = 'Your Email ...'
        self.fields['password1'].widget.attrs["class"] = 'form-control'
        self.fields['password1'].widget.attrs["placeholder"] = 'Your Password ...'
        self.fields['password2'].widget.attrs["class"] = 'form-control'
        self.fields['password2'].widget.attrs["placeholder"] = 'Confirm Your Password ...'
        self.fields['agree_terms'].widget.attrs["class"] = 'form-check-input'
    
    class Meta:
        model = Customer
        fields = ('username', 'email', 'agree_terms', 'password1', 'password2')