# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django import forms



class ShiftManager(models.Manager):
	def most_recent(self):
		return self.order_by('-start_datetime')
	def create_shift(self, start_datetime, end_datetime): # creating model instance 
		shift = self.create(start_datetime = runs_start.start_datetime, end_datetime = end_datetime)
		return shift

class Shift(models.Model):
	shifts_text = models.CharField(max_length=200)
	start_datetime = models.DateTimeField(blank=True, null=True)
	end_datetime = models.DateTimeField(blank=True,null =True)
	objects = ShiftManager()
	def __str__(self):
		return self.shifts_text
	
class Run(models.Model):
	shift = models.ForeignKey(Shift, related_name ="runs_related") # each run is related to a shift
	runs_text = models.CharField(max_length=200)
	runs_start = models.TimeField(blank=True, null=True)
	runs_end = models.TimeField(blank=True, null=True)
	user_id = models.IntegerField(default=0, blank=True)
	
	
	def __str__(self):
		return self.runs_text

class NewRunForm(forms.ModelForm):
	#runs_text = forms.CharField()
	#runs_end = forms.DateTimeField()
	class Meta:
		model = Run
		fields = ('runs_text',)