from django import forms
from .models import Movie
class Movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['Name','Desc','Year','Img']
