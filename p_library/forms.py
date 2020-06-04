from django import forms

from .models import Author, Reader


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'

class ReaderForm(forms.ModelForm):

    class Meta:
        model = Reader
        fields = '__all__'
