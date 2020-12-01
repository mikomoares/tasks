from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getTasks', views.get_tasks, name='get all tasks'),
    path('deleteTasks', views.delete_tasks, name='delete all tasks'),
    path('postTask', views.post_task, name='create new task')
]
