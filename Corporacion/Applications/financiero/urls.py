from django.urls import path
from . import views
app_name = 'finance_app'

urlpatterns = [
    path(
        'finance-list-invoice/',
        views.InvoiceListGeneral.as_view(), 
        name='finance-list-invoice'
    ),
    path(
        'finance-list-invoice-detail/<pk>/',
        views.InvoiceListviewUser.as_view(), 
        name='finance-list-invoice-detail'
    ),
    path(
        'finance-list-invoice-detail-up/<pk>/',
        views.InvoiceDetailView.as_view(), 
        name='finance-list-invoice-detail-up'
    ),
    path(
        'finance-list-invoice-sub/',
        views.InvoiceSubCreate.as_view(), 
        name='finance-list-invoice-sub'
    ),
    path(
        'finance-invoice-detail-more/',
        views.ListInvoiceDetailView.as_view(), 
        name='finance-invoice-detail-more'
    ),

    

    

    

    

    
  
  
]