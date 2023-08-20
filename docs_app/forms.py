from django import forms
from .models import Document , Category
class Document_Form(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ['author', 'created_at', 'category']