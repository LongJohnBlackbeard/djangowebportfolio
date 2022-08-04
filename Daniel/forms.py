from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):

    message = forms.CharField(widget=forms.Textarea(
        attrs={'name': 'Message', 'rows': 10, 'cols': 9}))

    class Meta:
        model = Contact
        fields = ['email', 'name', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {"class": "form-control", "placeholder": "email"}
        )
        self.fields['name'].widget.attrs.update(
            {"class": "form-control", "placeholder": "name"}
        )
        self.fields['message'].widget.attrs.update(
            {"class": "form-control", "placeholder": "message"}
        )
