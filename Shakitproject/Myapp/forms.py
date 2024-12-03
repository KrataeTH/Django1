from django import forms
from .models import Customer, Address, Subdistrict, District

class CustomerForm(forms.ModelForm):
    # Keep your existing field definitions
    address_text = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter address'}),
        required=True
    )
    
    subdistrict = forms.ChoiceField(
        choices=Subdistrict.choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    
    district = forms.ChoiceField(
        choices=District.choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Customer
        fields = ['name', 'customer_type', 'address_text', 'subdistrict', 'district', 'phone_number', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter customer name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'customer_type': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If editing an existing customer, pre-populate address fields
        if self.instance and self.instance.pk:
            if self.instance.address:
                self.fields['address_text'].initial = self.instance.address.address
                self.fields['subdistrict'].initial = self.instance.address.subdistrict
                self.fields['district'].initial = self.instance.address.district

    # Keep your existing validation and save methods
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) <= 8:
            raise forms.ValidationError('Phone number must be 9 digits')
        return phone_number

    def save(self, commit=True):
        # If the customer already has an address, update it
        if self.instance.pk and self.instance.address:
            address_instance = self.instance.address
            address_instance.address = self.cleaned_data['address_text']
            address_instance.subdistrict = self.cleaned_data['subdistrict']
            address_instance.district = self.cleaned_data['district']
            address_instance.save()
        else:
            # Create a new address if no existing address
            address_instance = Address.objects.create(
                address=self.cleaned_data['address_text'],
                subdistrict=self.cleaned_data['subdistrict'],
                district=self.cleaned_data['district']
            )
        
        # Save the customer
        customer = super().save(commit=False)
        customer.address = address_instance
        if commit:
            customer.save()
        return customer