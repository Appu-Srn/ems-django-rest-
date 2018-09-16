"""ems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from employee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('poll.urls')),
    path('employee/', include('employee.urls')),

    path('login/', login_view, name="login"),
    path('success/', success, name="user_success"),
    path('logout/', logout_view, name="user_logout"),
    path('profile/', ProfileUpdate.as_view(), name="my_profile"),
    path('profile/update', ProfileUpdate.as_view(), name="update_profile"),
]
