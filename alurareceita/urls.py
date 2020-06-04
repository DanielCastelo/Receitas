from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('receitas.urls')), #app receitas
    path('admin/', admin.site.urls),
]
