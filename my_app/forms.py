from django import forms
from .models import Changement, Incident, ITMFS
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ChangementForm(forms.ModelForm):
    class Meta:
        model = Changement
        fields = ['service_impacte', 'date_changement', 'duree_changement', 'destinataire', 'description', 'statut_changement']
        widgets = {
            'date_changement': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'duree_changement': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Duration in hours'}),
        }

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['service_impacted', 'destinataire', 'date', 'statut']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ITMFSForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
