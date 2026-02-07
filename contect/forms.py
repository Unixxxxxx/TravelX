from django import forms
from .models import InfoID


class InfoIDForm(forms.ModelForm):
    class Meta:
        model = InfoID
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
        }

