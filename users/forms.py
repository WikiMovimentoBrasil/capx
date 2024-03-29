from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {
            'birthday': forms.DateTimeInput(attrs={'type': 'date'})
        }
        exclude = ['user']  # Exclude user field since it's linked to CustomUser
