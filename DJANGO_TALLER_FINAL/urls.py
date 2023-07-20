"""
URL configuration for DJANGO_TALLER_FINAL project.

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
from django.contrib import admin
from django.urls import path
from gastronomica.views import index, guardar, verInscritos, inscrito_list, inscrito_detalle, InscritoList, InscritoDetalle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('guardar/', guardar),
    path('inscritos/', verInscritos),
    path('clase/', InscritoList.as_view()),
    path('clase/<int:pk>/', InscritoDetalle.as_view()),
    path('funcion/', inscrito_list),
    path('funcion/<int:id>', inscrito_detalle )
]
