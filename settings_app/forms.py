from django import forms
from settings_app.models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        exclude = ("date_sent", "accept")
