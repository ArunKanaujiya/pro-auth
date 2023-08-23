from django import forms
from WebApp.models import Book
class StdForm(forms.Form):
    class Meta:
        model=Book
        fields='__all__'