"""monitoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('', include('measurements.urls')),
    path('', include('devices.urls'), namespace='devices'),
    path('', include('variables.urls'), namespace='variables'),
    path('', include('sites.urls'), namespace='sites'),
    path('', include('medicines.urls'), namespace='medicines'),
    path('', include('diagnostics.urls'), namespace='diagnostics'),
    path('', include('symptoms.urls'), namespace='symptoms'),
    path('', include('vitalSigns.urls'), namespace='vitalSigns'),
    path('', include('entrys.urls'), namespace='entrys'),
    path('health-check/', views.healthCheck),
]
