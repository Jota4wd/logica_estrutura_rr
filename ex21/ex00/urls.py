from django.contrib import admin
from django.urls import path
from .views import ola
from .views import horas

urlpatterns = [
    path("admin/", admin.site.urls),
    path('ola/', ola, name='ola'),
    path('horas/', horas, name = 'horas'),
]

