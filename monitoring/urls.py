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
    #path('', include('measurements.urls')),
    path('', include(('devices.urls','devices'), namespace='devices')),
    path('', include(('variables.urls','variables'), namespace='variables')),
    path('', include(('sites.urls','sites'), namespace='sites')),
    path('', include(('medicines.urls','medicines'), namespace='medicines')),
    path('', include(('diagnostics.urls','diagnostics'), namespace='diagnostics')),
    path('', include(('symptoms.urls','symptoms'), namespace='symptoms')),
    path('', include(('vitalSigns.urls','vitalSigns'), namespace='vitalSigns')),
    path('', include(('entrys.urls','entrys'), namespace='entrys')),
    path('', include(('devices.urls','create_device'), namespace='deviceCreate')),
    path('health-check/', views.healthCheck),
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),
    
]
