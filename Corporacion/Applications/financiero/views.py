from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic import (TemplateView, 
FormView, CreateView, DeleteView, UpdateView,
DetailView, ListView, View)
from django.db.models import Count, Sum
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models.functions import Coalesce

from Applications.academico.models import Estudiante
from .models import *
from .forms import *



class InvoiceListGeneral(ListView):
    model = Facturas
    template_name = 'Financiero/Listinvoicesgeneral.html' 
    context_object_name = 'invoice'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(InvoiceListGeneral, self).get_context_data(**kwargs)
        usuario = list(Facturas.objects.all().values("user").distinct())
        datos=[]

        for i in usuario:
            
            pendiente = Facturas.objects.filter(user= i['user'], estado_id=1).count()
            pagadas = Facturas.objects.filter(user= i['user'], estado_id=2).count()
            abono = Facturas.objects.filter(user= i['user'], estado_id=3).count()
            data_final = {"Codigo": str(User.objects.get(codigo=i['user']).codigo), "Usuario":str( User.objects.get(codigo=i['user']).nombres)+ " "+str(User.objects.get(codigo=i['user']).apellidos),"Pagadas":pagadas, "Pendientes":pendiente, "Abonadas":abono}
            datos.append(data_final)

        context['student'] = datos
        return context


class InvoiceListviewUser(ListView):
    model = Facturas
    template_name = 'Financiero/Listinvoices.html' 
    context_object_name = 'invoice'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(InvoiceListviewUser,self).get_context_data(**kwargs)
        context["datos"] =Estudiante.objects.filter(codigo=self.kwargs['pk'])
        return context
    

    def get_queryset(self):
        info = []

        datos = Facturas.objects.filter(user=self.kwargs['pk']).order_by("codigo")
        
        for i in datos:
            pagado=FacturasSub.objects.filter(facturas_id=i.pk).aggregate(Sum('pagado'))
            pagados_data=FacturasSub.objects.filter(facturas_id=i.pk)
            datos_final= {'pk':i.pk, "codigo":i.codigo, 'descripcion':i.descripcion, 'estado':i.estado, 'monto':i.monto, 'pagado':pagado['pagado__sum']}
            
            info.append(datos_final)
        return info

class ListInvoiceDetailView(View):
    
    def get(self, request, *args, **kwargs):
        info = []
        pagados_data=FacturasSub.objects.filter(facturas_id=Facturas.objects.get(id=int(self.request.GET.get('info'))) )
        
        for e in pagados_data:
            datos={'consecutivo':e.consecutivo,'observacion':e.observacion, 'payed':e.pagado, 'fecha': str(e.created_at.day) + "-" + str(e.created_at.month) +"-"+ str(e.created_at.year)}
            info.append(datos)
        response = {}
        response['data']=info
        return JsonResponse(response)
        

class InvoiceDetailView(FormView):

    template_name = 'Financiero/update_invoice.html'
    model = Facturas
    form_class= FacturasForm

    def get_context_data(self, **kwargs):
        context = super(InvoiceDetailView,self).get_context_data(**kwargs)
        pagado= FacturasSub.objects.filter(facturas_id=self.kwargs['pk']).aggregate(Sum('pagado'))
        data = Facturas.objects.get(pk=self.kwargs['pk'])
        datos=[]
        info = {"codigo":data.codigo, "monto": data.monto, 'pagado': Facturas.objects.manejo2(pagado), 'pendiente':Facturas.objects.manejo(data, pagado)}
        datos.append(info)
        context["datos"]= datos
        return context
    
    
class InvoiceSubCreate(View):

    def post(self, request, *args, **kwargs):

        facturas = self.request.POST.get('facturas')
        observacion = self.request.POST.get('observacion')
        consecutivo = self.request.POST.get('consecutivo')
        pagado = self.request.POST.get('pagado')

        if FacturasSub.objects.filter(consecutivo = consecutivo) or Gastos.objects.filter(consecutivo = consecutivo):
            messages.warning(self.request,'El consecutivo que intenta crear ya existe, por favor verifique el número del recibo de pago')
            return HttpResponseRedirect(self.request.META.get("HTTP_REFERER"))

        else:
            matricula= FacturasSub.objects.create(
                facturas=Facturas.objects.get(codigo=facturas),
                observacion=observacion,
                consecutivo=consecutivo,
                pagado=pagado,
            )
            fact_act = FacturasSub.objects.filter(facturas_id=Facturas.objects.get(codigo=facturas).id).aggregate(Sum('pagado'))
            monto=Facturas.objects.get(codigo=facturas).monto
            if int(fact_act['pagado__sum']) == int(monto):
                Facturas.objects.filter(codigo=facturas).update(estado_id=CatalogsTypesInvoices.objects.get(estado="Pagada"))
            elif int(fact_act['pagado__sum']) > 0  and int(fact_act['pagado__sum']) < int(monto):
                Facturas.objects.filter(codigo=facturas).update(estado_id=CatalogsTypesInvoices.objects.get(estado="Abono"))
            else:
                Facturas.objects.filter(codigo=facturas).update(estado_id=CatalogsTypesInvoices.objects.get(estado="Pendiente"))

            return HttpResponseRedirect( reverse_lazy('finance_app:finance-list-invoice'))