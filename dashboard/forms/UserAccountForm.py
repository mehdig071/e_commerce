from django import forms
from accounts.models.Customer import Customer

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('username', 'first_name', 'last_name', 'email')
        
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control custom-text-input'}),
        }
