from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('devices/', views.device_list),
    path('deviceSede/', views.getSede),
    #path('create_device/', views.create_device),
    path('create_device/', views.device_create),
]