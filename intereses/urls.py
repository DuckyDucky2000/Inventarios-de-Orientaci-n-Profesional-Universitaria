from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index),
    path('', views.intereses, name="intereses"),
]