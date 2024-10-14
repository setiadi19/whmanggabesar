from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Mengarahkan ke app home
    path('login/', include('login.urls')),  # Untuk halaman login dan logout
    path('dashboard/', include('dashboard.urls')),  # Untuk halaman dashboard
]
