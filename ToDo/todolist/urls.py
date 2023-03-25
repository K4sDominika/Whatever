from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

from .views import CreateTask,DeleteTask,UpdateTask, TaskList,OverviewTask, LoginUser, RegisterUser


urlpatterns = [
    path('', views.index, name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

    path('list/', TaskList.as_view(), name='list'),
    path('task/<int:pk>/', OverviewTask.as_view(), name='task'),
    path('createTask/', CreateTask.as_view(), name='createTask'),
    path('deleteTask/<int:pk>/', DeleteTask.as_view(), name='deleteTask'),
    path('updateTask/<int:pk>/', UpdateTask.as_view(), name='updateTask'),

]
