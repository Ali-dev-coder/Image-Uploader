from django import forms
from django.db.models import fields

from .models import imagemodel
class imageforms(forms.ModelForm):
    class Meta:
        model = imagemodel
        fields = '__all__'
        labels = {'photo':''}