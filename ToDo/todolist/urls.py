from django.urls import path

from . import views

from .views import CreateTask,DeleteTask,UpdateTask, TaskList,OverviewTask


urlpatterns = [
    path('', views.index),
    path('list/', TaskList.as_view(), name='list'),
    path('task/<int:pk>/', OverviewTask.as_view(), name='task'),
    path('createTask/', CreateTask.as_view(), name='createTask'),
    path('deleteTask/<int:pk>/', DeleteTask.as_view(), name='deleteTask'),
    path('updateTask/<int:pk>/', UpdateTask.as_view(), name='updateTask'),

]
