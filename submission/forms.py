# submission/forms.py
from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['image', 'full_name', 'address', 'email', 'phone' , 'personal_details']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'address': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Your address'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Optional phone number'}),
            'personal_details': forms.TextInput(attrs={'placeholder': 'Tell me about yourself'}),
        }
