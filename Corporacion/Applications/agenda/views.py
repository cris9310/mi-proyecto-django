from datetime import datetime, date
from time import strptime
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.writer.excel import save_virtual_workbook
from decimal import *


from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy

from .forms import AgendaRegisterForm
from .models import *
from django.views.generic import (TemplateView, 
FormView, CreateView, DeleteView, UpdateView,
DetailView, ListView, View)



class EventCreateView(FormView):
    form_class = AgendaRegisterForm
    template_name = 'Agenda/register_event.html'
    success_url =  reverse_lazy('academico_app:list-student')

    def form_valid(self, form): 


        form = AgendaRegisterForm(self.request.POST)
        
        if form.is_valid():
            create_student= Evento.objects.create(
                user= self.request.user,
                title=form.cleaned_data['title'],
                descripcion= form.cleaned_data['descripcion'],
                start_time=str(form['start_time'].value()),
                end_time=str(form['end_time'].value()),
                color = form['color'].value(),
                hora_inicio=str(form['hora_inicio'].value()),
                hora_final=str(form['hora_final'].value()),
            )
        return HttpResponseRedirect(self.success_url)
    
class EventoUpdateView(UpdateView):
    model = Evento
    template_name = 'Agenda/update_event.html'
    form_class = AgendaRegisterForm
    success_url = reverse_lazy('academico_app:dashboard')

class EventoDeleteView(DeleteView):
    template_name = 'Agenda/delete_event.html'
    model = Evento
    success_url = reverse_lazy('academico_app:dashboard')