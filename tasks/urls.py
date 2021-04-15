"""todo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>/', views.taskView, name="task-view"),
    path('newtask/', views.newTask, name="new-task"),
    path('edittask/<int:id>/', views.editTask, name="edit-task"),
    path('yourname/<str:name>/', views.yourName),
]
