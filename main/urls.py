from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('', views.home, name="home"),
    path('event_menu', views.event_menu, name="event_menu"),

    path('event_reg_modal/<str:pk>', views.event_reg_modal, name="event_reg_modal"),
    path('event_reg/<str:pk>', views.event_reg, name="event_reg"),

    path('404', views.unavailable_page, name="unavailable_page"),
]
