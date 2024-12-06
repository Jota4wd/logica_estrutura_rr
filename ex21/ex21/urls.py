from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('ex00/', include('ex00.urls')),
    path('ex01/', include('ex01.urls')),
]
