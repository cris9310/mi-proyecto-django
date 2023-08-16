from django.urls import path
from . import views
app_name = 'agenda_app'

urlpatterns = [
    path(
        'create-event/',
        views.EventCreateView.as_view(), 
        name='create-event'
    ),
    path(
        'update-event/<pk>/',
        views.EventoUpdateView.as_view(), 
        name='update-event'
    ),
    path(
        'delete-event/<pk>/',
        views.EventoDeleteView.as_view(), 
        name='delete-event'
    ),

    
  
  
]