# users/forms.py
from django import forms
from .models import DocumentVerification

class DocumentVerificationForm(forms.ModelForm):
    class Meta:
        model = DocumentVerification
        #fields = '__all__'
        exclude = ('process_complete','verified')
    