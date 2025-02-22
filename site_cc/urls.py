from django.urls import path
from . import views
from .views import mainpage_view 
from .views import homepage_view
from .views import  salvar_selecao_modal
from .views import api_weather

from  Plantae.views import DashboardView


app_name = "site_cc"

urlpatterns = [
    path("", homepage_view, name="homepage"),
    path("mainpage/", mainpage_view, name="mainpage"),
    path("calender/", views.calendar_view_new, name="calendar"),
    path("calenders/", views.calendar_view, name="calendars"),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('next_week/<int:event_id>/', views.next_week, name='next_week'),
    path('next_day/<int:event_id>/', views.next_day, name='next_day'),
    path("event/new/", views.create_or_edit_event, name="event_new"),
    path("event/new/plantio/", views.create_plantio_event, name="event_new_plantio"),  # Nova URL para eventos de Plantio
    path("event/<int:event_id>/details/", views.event_details, name="event-detail"),
    path("add_eventmember/<int:event_id>", views.add_eventmember, name="add_eventmember"),       
    path("event/<int:pk>/remove", views.event_member_delete, name="remove_event"),
    path("all-event-list/", views.all_events_list, name="all_events"),    
    path("running-event-list/", views.running_events_list, name="running_events"), 
    path('praga/', views.praga, name='praga'),
    path('detalhes_problema/', views.detalhes_problema, name='detalhes_problema'),
    path('recomendacao/', views.recomendacao, name='recomendacao'),
    path('detectar_pragas_doencas/', views.detectar_pragas_doencas, name='detectar_pragas_doencas'),
    path("event/plantio/<int:plantio_event_id>/create_colheita/", views.create_colheita_event, name="create_colheita_event"),
    path('alerta_colheita', views.alerta_colheita, name='alerta_colheita'),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path('listar-problemas/', views.listar_problemas, name='listar_problemas'),
    path('url-salvar-selecao-modal/', salvar_selecao_modal, name='salvar_selecao_modal'),
    path('api/events/', views.api_events, name='api_events'),
    path('planta_detalhes/', views.planta_detalhes, name='planta_detalhes'),
    path('preferences/', views.preferences_view, name='preferences'),
    path('logout/', views.logout_view, name='logout'),
    path('api/weather/', api_weather, name='api_weather'),
    path('preferences/', views.preferences_view, name='preferences'),
    



]
