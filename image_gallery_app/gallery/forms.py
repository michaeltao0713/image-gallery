from django import forms
from .models import Tags


class AddTagForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), required=False)


class FilterForm(forms.Form):
    tag = forms.ModelChoiceField(queryset=Tags.objects.all(), required=False, label='Filer by Tag')
    