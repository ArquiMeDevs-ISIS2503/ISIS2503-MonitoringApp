from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('vitalSigns/', views.vitalSign_list, name='vitalSignList'),
    path('vitalSigncreate/', csrf_exempt(views.vitalSign_create), name='vitalSignCreate'),
]