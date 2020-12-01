from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getTasks', views.index, name='get all tasks'),
    path('deleteTasks', views.index, name='delete all tasks'),
    path('postTask', views.index, name='create new task')
]
