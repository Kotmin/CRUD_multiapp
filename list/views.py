from django.shortcuts import render
from django.http import HttpResponse # just for debug purposes


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class TaskList(LoginRequiredMixin,ListView):
    model = Task # req model or query set
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        #context['count'] = context['tasks'].filter(complete=False).count()
        return context

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'list/task.html' # path lib!!!

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    #fields = '__all__' # alt =['title','desc]
    fields = ['title','description','state']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)
    
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')