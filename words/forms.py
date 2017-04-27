from django.forms import ModelForm, Textarea
from .models import Word, Media

class WordsForm( ModelForm ):
    class Meta:
        model   = Word

class MediaForm(ModelForm):
    class Meta:
        model   = Media
