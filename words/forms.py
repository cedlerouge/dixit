from django.forms import ModelForm, Textarea
from .models import Word, Media

class WordForm( ModelForm ):
    class Meta:
        model   = Word
        fields  = '__all__'

class MediaForm(ModelForm):
    class Meta:
        model   = Media
        fields  = '__all__'
