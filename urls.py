"""multiuser_todoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from todo.views import index,addTodo, deleteTodo
from login.views import start_page, register

urlpatterns = [
    path('', start_page, name = 'start_page'),
    path('todo/<username>/', index, name = 'todo_view'),
    path('accounts/', include('django.contrib.auth.urls'), name = 'accounts'),
    path('admin/', admin.site.urls),
    path('register/', register, name = 'register'),
    path('addTodo/<username>', addTodo, name = 'addTodo'),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
]
