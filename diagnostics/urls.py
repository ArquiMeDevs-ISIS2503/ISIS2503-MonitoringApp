from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('diagnostics/', views.diagnostic_list, name='diagnosticList'),
    path('diagnosticcreate/', csrf_exempt(views.diagnostic_create), name='diagnosticCreate'),
]