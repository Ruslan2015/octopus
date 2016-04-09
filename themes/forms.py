from django import forms
#from .models import Themes


class FilterThemes(forms.Form):
#     number = forms.CharField(label="Номер", max_length=10)
    name = forms.CharField(label="Тема", max_length=10)
        