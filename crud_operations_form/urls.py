"""
URL configuration for crud_operations_form project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addprod_view/',addprod_view),
    path('',home),
    path('listprod_view/',listprod_view),
    path('prodedit_view/<pid>/',prodedit_view),
    path('saveeditedprod_view/',saveeditedprod_view),
    path('proddelete_view/<pid>/',proddelete_view)
]
