from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from accounts.models.Customer import Customer

class CustomLoginForm(AuthenticationForm):
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs["class"] = 'form-control'
        self.fields['username'].widget.attrs["placeholder"] = 'Your Username ...'
        self.fields['password'].widget.attrs["class"] = 'form-control'
        self.fields['password'].widget.attrs["placeholder"] = 'Your Password ...'
    