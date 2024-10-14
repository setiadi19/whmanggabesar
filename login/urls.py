from django.urls import path
from . import views



urlpatterns = [
    path('', views.user_login, name="login"),  # Login URL
    path('logout/', views.user_logout, name="logout"),  # Logout URL
]
