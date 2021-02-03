from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('', views.home, name="home"),
    path('event_menu', views.event_menu, name="event_menu"),

    path('event_reg_modal/<str:pk>', views.event_reg_modal, name="event_reg_modal"),
    path('event_reg/<str:pk>', views.event_reg, name="event_reg"),

    path('pt_event_status_modal/<str:pk>', views.pt_event_status_modal, name="pt_event_status_modal"),
    path('pt_event_status/<str:pk>', views.pt_event_status, name="pt_event_status"),

    path('pt_event_feedback_modal/<str:pk>', views.pt_event_feedback_modal, name="pt_event_feedback_modal"),
    path('pt_event_feedback/<str:pk>', views.pt_event_feedback, name="pt_event_feedback"),

    path('event_management', views.pt_event_mngt, name="pt_event_mngt"),

    path('cl/event_management', views.cl_event_mngt, name="cl_event_mngt"),
    path('cl/create_event', views.cl_create_event, name="cl_create_event"),
    path('cl/event_proposal', views.event_proposal, name="event_proposal"),

    path('pm/event_proposal', views.event_proposal, name="event_proposal"),




    path('404', views.unavailable_page, name="unavailable_page"),
]
