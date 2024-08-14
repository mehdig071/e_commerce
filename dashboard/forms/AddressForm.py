from django import forms
from dashboard.models.Address import Address

class AddressForm(forms.ModelForm):
    ADDRESS_TYPE_CHOICES = [('billing', 'Billing'), ('shipping', 'Shipping')]
    
    address_type = forms.ChoiceField(
        choices=ADDRESS_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control custom-text-input'})
    )
    class Meta:
        model = Address
        fields = ('name', 'full_name', 'street', 'code_postal', 'city', 'country', 'more_details', 'address_type')

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'full_name' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'street' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'code_postal' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'city' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'country' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'more_details' : forms.Textarea(attrs={'class': 'form-control custom-textarea'}),
        }
