from django.shortcuts import render
from django.http import HttpResponse # just for debug purposes


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from .models import Task

#Auto translation part
from django.utils.translation import gettext as _



# Create your views here.


def throw_HTTP(request):
    """
    Main functionality returns a HTTPresponce
    """
    # Translators: This message shoudl appear only while logged on the main app page
    output = _("Your todo list")
    return HttpResponse(output)



class CustomLoginView(LoginView):
    template_name = 'list/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('tasks')

class TaskList(ListView):
    model = Task # req model or query set
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'list/task.html' # path lib!!!

class TaskCreate(CreateView):
    model = Task
    fields = '__all__' # alt =['title','desc]
    success_url = reverse_lazy('tasks')
    
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')