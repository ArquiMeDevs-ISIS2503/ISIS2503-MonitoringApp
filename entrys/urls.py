from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('entrys/', views.entry_list, name='entryList'),
    path('entrycreate/', csrf_exempt(views.entry_create), name='entryCreate'),
]