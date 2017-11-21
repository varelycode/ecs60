# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Shift, Run



class RunInLine(admin.TabularInline):
	model = Run
	extra = 2


class ShiftAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['shifts_text']}),
        ('Shift information', {'fields': ('start_datetime','end_datetime')}),
    ]
    
	inlines = [RunInLine]
	list_display = ('shifts_text', 'start_datetime', 'end_datetime')
	search_fields = ['shifts_text']

admin.site.register(Shift, ShiftAdmin)

# Register your models here.
