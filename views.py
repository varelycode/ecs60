from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views import generic
from django.utils import timezone
from datetime import datetime 
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django import forms
from .models import Shift, Run, NewRunForm



class IndexView(generic.ListView):
    template_name = 'shifts/index.html'
    context_object_name = 'latest_shifts_list'

    def get_queryset(self):
        return Shift.objects.most_recent()

class ResultsView(generic.DetailView):
    model = Shift
    template_name = 'shifts/results.html'
    
class DetailView(generic.DetailView):
   model = Shift
   template_name = 'shifts/detail.html'

def create_run(request, shift_id):
	if request.method == 'POST':
		form = NewRunForm(request.POST)
		if form.is_valid():
			new_obj = form.save(commit=False)
			new_obj.run = request.run
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = NewRunForm()
	return render(request, 'shifts/results.html', {'form': form})