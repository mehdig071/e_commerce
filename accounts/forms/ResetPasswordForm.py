from django import forms
from accounts.models.Customer import Customer
from django.contrib.auth import authenticate

class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        fields = ('old_password', 'new_password1', 'new_password2')
        
       
    def clean(self):
        cleaned_data = super().clean()
        old_password =  cleaned_data.get('old_password')
        new_password1 =  cleaned_data.get('new_password1')
        new_password2 =  cleaned_data.get('new_password2')
        
        user = self.user
        
        user_authenticated = authenticate(username=user.username, password=old_password)
        
        if not user_authenticated:
            self.add_error('old_password', 'Incorrect old password. Please try again.')
        
        if new_password1 != new_password2:
            self.add_error('new_password2', 'New passwords do not match.')
            
        return cleaned_data