"""
URL configuration for update project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import statistics
from tracemalloc import Statistic
from django.contrib import admin
from django.urls import include, path

from update import settings
# add the authantication app url inside the urlpatterns 2nd path 
#goto the create tha url.py inside the auth app



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('authentication.urls')),
]



urlpatterns += statistics(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += Statistic(settings.STATIC_URL, document_root=settings.STATIC_ROOT)