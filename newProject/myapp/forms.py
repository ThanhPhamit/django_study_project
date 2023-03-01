from django import forms

from .models import Loggeṛ


class LogForm(forms.ModelForm):
    class Meta:
        model = Loggeṛ
        fields = '__all__'
