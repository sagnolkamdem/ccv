from django import forms
from .models import Contact


# Create your forms here.

class ContactForm(forms.Form):
    nom_contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  label="Votre nom",
                                  max_length=200)
    prenom_contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                     label="Votre prenom",
                                     max_length=200)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                             label="Votre adresse e-mail",
                             required=True)
    messagees = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),
                                label="Votre message")