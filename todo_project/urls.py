"""
URL configuration for todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from tasks.views import *

urlpatterns = [
    #http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8000/ -> ozon.ru
    path('', home, name='home'),
    #http://127.0.0.1:8000/create/
    path('create/', create_task),
    #http://127.0.0.1:8000/delete/9
    path('delete/<int:id>/', delete_task, name='delete'),
    #http://127.0.0.1:8000/delete/9
    path('complete/<int:id>/', complete_task, name='complete')
]
