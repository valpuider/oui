from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    mot_de_passe = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['nom', 'prénom', 'email', 'sexe', 'mot_de_passe', 'pseudonyme', 'date_naissance']
