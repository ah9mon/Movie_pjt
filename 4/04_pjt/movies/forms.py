from django import forms
from .models import Movie
from django.forms.widgets import Select, DateInput

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'score': forms.NumberInput(attrs={'step': 0.5}),
            'genre': Select(choices=Movie.GENRE_CHOICES),
            'release_date': DateInput(),
        }