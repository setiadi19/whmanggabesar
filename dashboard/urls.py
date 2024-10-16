
from django.urls import path
from . import views  # Mengimpor semua dari views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # URL untuk dashboard
    path('send_notification/', views.send_notification, name='send_notification'),  # Mengakses send_notification dari views
]
