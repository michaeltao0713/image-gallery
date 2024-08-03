from django import forms
from .models import Tags


class AddTagForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), required=False)
