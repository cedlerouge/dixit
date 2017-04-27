from django.contrib import admin
from .models import Word, Profile, Media
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class ProfileInline(admin.StackedInline):
    model               = Profile
    verbose_name_plural = 'Profile'
    fk_name             = 'user'


class CustomUserAdmin(UserAdmin):
    inlines     = (ProfileInline,)
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class WordsAdmin(admin.ModelAdmin):
    list_filter     = ('author', 'context')
    ordering        = ('-date', 'author')
    search_fields   = ('date ', 'author')

    def author(self, obj):
        return obj.author

class MediaAdmin(admin.ModelAdmin):
    list_filter = ("user", "word")
    
    def user(self, obj):
        return obj.user


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Word, WordsAdmin)
admin.site.register(Media, MediaAdmin)
