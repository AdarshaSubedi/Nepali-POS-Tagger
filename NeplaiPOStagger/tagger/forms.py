from django import forms
from .models import Paragraph




class ParagraphForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter nepali text'}))

    class Meta:
        model = Paragraph
        fields = ['text']