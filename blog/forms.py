from django import forms
from .models import *
from django.db import models


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label=u"Votre adresse mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

    def clean_message(self):
        message = self.cleaned_data['message']
        if "Petasse" in message:
            raise forms.ValidationError("Le mot petasse est interdit")
        return message

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if sujet and message:
            if "petasse" in sujet and "petasse" in message:
                alert = "!!!!!!  enleves le petasse la sur le champs en dessous !!!!!!"
                self._errors["message"] = self.error_class([alert])

                del cleaned_data["message"]

                self._errors["sujet"] = self.error_class([alert])

                del cleaned_data["sujet"]
        return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('__all__')


class ContactImForm(forms.ModelForm):
    class Meta:
        model = contact_image
        fields = ('__all__')