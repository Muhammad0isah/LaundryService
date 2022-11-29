from django import forms
from django.forms import TextInput

from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email','subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control valid', 'placeholder': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control valid', 'placeholder': 'email'}),
            'subject': TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'message': forms.Textarea(attrs={'class': 'form-control w-100', 'placeholder': 'message'}),

        }
