from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_complaint', views.create_complaint, name='create_complaint'),
]