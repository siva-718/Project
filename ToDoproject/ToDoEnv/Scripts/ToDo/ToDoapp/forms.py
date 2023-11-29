from .models import TODO
from django import forms
class ToDoForm(forms.ModelForm):
    class Meta:
        model=TODO
        fields=['Task','Priority','Date']