from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('medicines/', views.medicine_list, name='medicineList'),
    path('medicinecreate/', csrf_exempt(views.medicine_create), name='medicineCreate'),
]