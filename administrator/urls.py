from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    # path('404', views.unavailable_page, name="unavailable_page"),
]
