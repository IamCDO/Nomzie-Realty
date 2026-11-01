from django.contrib import admin
from django.urls import path

from .views import home, property_detail

urlpatterns = [
    path('', home, name='home'),
    path('property/<slug:slug>/', property_detail, name='property_detail'),
    path('admin/', admin.site.urls),
]
