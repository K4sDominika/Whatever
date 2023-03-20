from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.list import ListView

from .forms import NewUserCreationForm
# Create your views here.
from .models import Task


def index(request):
    return render(request, 'home.html')


class LoginUser(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(FormView):
    template_name = 'register.html'
    form_class = NewUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')



# def task_list(request):
# tasks = Task.objects.all()

# context = {'tasks': tasks}
# return render(request, 'task_list.html', context)

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'


class OverviewTask(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_overview.html'


class CreateTask(CreateView):
    model = Task
    fields = '__all__'

    template_name = 'create_task.html'

    success_url = reverse_lazy('list')


class DeleteTask(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('list')


class UpdateTask(UpdateView):
    model = Task
    template_name = 'task_update.html'
    fields = '__all__'
    success_url = reverse_lazy('list')
