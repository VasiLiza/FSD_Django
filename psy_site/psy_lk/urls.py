from django.urls import path
from .main.a_pages import views as a_pages_views
from .main.c_features import views as c_features_views
urlpatterns = [
    path('', a_pages_views.index, name='index'),

    path('c_features/create_complaint', c_features_views.create_complaint, name='create_complaint'),
    path('c_features/card_panel', c_features_views.card_panel, name='card_panel'),
]