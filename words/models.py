from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Word( models.Model ):
    user    = models.CharField(max_length=30,default='anonymous')
    date    = models.DateTimeField(auto_now_add=True)
    context = models.CharField(max_length=200,default='ladiici')
    words   = models.CharField(max_length=500,default='ladi')
    author  = models.CharField(max_length=500,default='ladilafe')

class Profile(models.Model):
    user            = models.OneToOneField( User, on_delete=models.CASCADE)
    is_admin        = models.BooleanField(default=False)
    tz              = models.CharField(max_length=30,default='Europe/Paris')
    points_won      = models.IntegerField( null=True, default=0 )

class Media(models.Model):
    user    = models.ForeignKey(Profile)
    word    = models.ForeignKey(Word, on_delete=models.CASCADE)
    images  = models.ImageField(upload_to="img/", null=True)
    #TODO A voir pour ajouter d'autres medias (videos, audios)
    #TODO liens externe avec visualisation dans le site
    # audio_file = models.FileField(upload_to = u'mp3/', max_length=200)
    # video_file = models.FileField(upload_to = u'video/', max_length=200)
