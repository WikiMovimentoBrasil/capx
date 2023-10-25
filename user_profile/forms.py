from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username','groups', 'pronoun', 'profile_image', 'first_name', 'middle_name', 'last_name', 'display_name', 'birthday', 'twitter', 'facebook','instagram','email','contact_method','region', 'language','affiliation','wikimedia_project','area_of_interest','skills_known', 'skills_wanted']