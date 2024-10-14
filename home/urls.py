from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pivot/', views.pivot, name='pivot'),  # Rute untuk pivot.html
]

