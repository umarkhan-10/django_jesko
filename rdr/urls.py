from django.urls import path
from . import views

urlpatterns = [
    path('', views.rdr, name='rdr'),
]