from django import forms
from django.forms.widgets import Textarea




class CollectionForm(forms.Form):
    text_area = forms.CharField(label='My Test Area', widget=Textarea({'id':'myTextarea'}))
