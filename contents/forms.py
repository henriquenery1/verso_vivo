from django import forms
from contents.models.content import Content

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'body']
