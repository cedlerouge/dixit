from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from django.utils import timezone
from words.model import Word
from .forms import WordForm


import logging                              
logger = logging.getLogger('dixi')        
logger.setLevel( logging.DEBUG )            
logger.addHandler( logging.StreamHandler() )

# Create your views here.

class Index( View ): 
    def get( self, reqquest ):
        params  = {'error_message': None }
        w       = Word.objects.order_by('-date')
        params['word'] = w
        return render( request, 'words/display_words.html', params )


class WordsView( View ):
    def get( self, request, word_id = None ):
        params  = {'error_message': None }
        form    = None
        if word_id:
            w       = get_object_or_404( Word, pk = word_id )
            user    = User.objects.get( username = request.user.username )
            if user.is_staff:
                form    = WordForm( instance = w )
                params['form']      = form
                params['post_url']  = reverse( 'words:word_add', args=(words_id)) 
                return render( request, 'words/word_form.html', params )
        #TODO else:
            # presenter un template contenant un message invitant à s'authentifier'

    def post( self, resquest, word_id = None ):
        
