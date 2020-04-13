from django.contrib import admin
from .models import *


class PhraseInfo(admin.ModelAdmin):
    list_display = ['id', 'phrase']
    search_fields = ['phrase']
    raw_id_fields = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7')
    list_per_page = 20
    fieldsets = [
        ('词组', {'fields': ['phrase']}),
        ('倒序字', {'fields': ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7']})
    ]
    ordering = ('id',)


class CharacterInfo(admin.ModelAdmin):
    list_display = ['id', 'character', 'csm', 'cym', 'tone', 'rhyme']
    fieldsets = [
        ('字', {'fields': ['character', 'csm', 'cym', 'tone', 'rhyme']}),
    ]
    search_fields = ['character']
    list_per_page = 20
    ordering = ('id',)


admin.site.site_header = '押韵短语管理系统'
admin.site.site_title = '押韵管理'

admin.site.register(Phrase, PhraseInfo)
admin.site.register(Character, CharacterInfo)
