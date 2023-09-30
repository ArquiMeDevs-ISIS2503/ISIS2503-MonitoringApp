from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('devices/', views.device_list),
    path('devices/deviceSede/', views.device_list),
    path('devicecreate/', csrf_exempt(views.device_create), name='deviceCreate'),
]