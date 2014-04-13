from django.contrib import admin
from models import *

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class PollAdmin(admin.ModelAdmin):
    list_display = ('question','name', 'was_published_recently')
    list_filter = ['question', 'name']
    search_fields = ['question', 'name']
    fieldsets = [
            (None, {'fields': ['name']}),
            (None, {'fields': ['pub_date']}),
            ('Question information', {'fields': ['question'], 'classes': ['collapse']}),
        ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
