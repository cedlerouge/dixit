from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect

from django.utils import timezone
from .models import Word
from .forms import WordForm


import logging                              
logger = logging.getLogger('dixi')        
logger.setLevel( logging.DEBUG )            
logger.addHandler( logging.StreamHandler() )

# Create your views here.

class Index( View ): 
    def get( self, request ):
        params  = {'error_message': None }
        w       = Word.objects.order_by('-date')
        params['words'] = w
        return render( request, 'word/display_words.html', params )


class WordView( View ):
    def get( self, request, word_id = None ):
        params  = {'error_message': None }
        form    = None
        if word_id:
            w       = get_object_or_404( Word, pk = word_id )
            #TODO manage authentication
            #user    = User.objects.get( username = request.user.username )
            #if user.is_staff:
            form    = WordForm(instance = w)
        else:
            form    = WordForm()
        params['form']      = form
        params['post_url']  = reverse( 'word_add', args=(word_id)) 
        return render( request, 'word/word_form.html', params )
        #TODO else:
            # presenter un template contenant un message invitant à s'authentifier'

    def post( self, request, word_id = None ):
        form    = WordForm(request.POST)
        if form.is_valid():
            w   = Word()
            w.author    = form.cleaned_data['author']
            #w.date      = form.cleaned_data['date']
            w.context   = form.cleaned_data['context']
            w.user      = form.cleaned_data['user']
            w.words     = form.cleaned_data['words']
            w.save()
            return HttpResponseRedirect( reverse('home'))
        return render( request, 'word/word_form.html', { 'form': form } )
