from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('', views.home, name="home"),
    path('event_menu', views.event_menu, name="event_menu"),
    # path('404', views.unavailable_page, name="unavailable_page"),
]
