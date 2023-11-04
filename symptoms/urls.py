from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('symptoms/', views.symptom_list, name='symptomList'),
    path('symptomcreate/', csrf_exempt(views.symptom_create), name='symptomCreate'),
]