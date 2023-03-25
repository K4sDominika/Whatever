from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
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

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('list')
        return super(RegisterUser, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context

    # class CompletedList(LoginRequiredMixin, ListView):
    #     model = Task


def completed(request):
    completed_tasks = Task.objects.filter(completed=True)
    template = loader.get_template('task_completed.html')
    context = {
        'tasks': completed_tasks
    }
    return HttpResponse(template.render(context, request))


class OverviewTask(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    fields = '__all__'
    template_name = 'task_overview.html'


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'

    template_name = 'create_task.html'

    success_url = reverse_lazy('list')


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('list')


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_update.html'
    fields = '__all__'
    success_url = reverse_lazy('list')
