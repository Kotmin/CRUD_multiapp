from django.shortcuts import render,redirect
from django.http import HttpResponse # just for debug purposes


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from django.views import View

from .models import Task

from django import forms

#Auto translation part
from django.utils.translation import gettext as _

#debugging
from django.template import loader

# Create your views here.


def throw_HTTP(request):
    """
    Main functionality returns a HTTPresponce
    """
    # Translators: This message shoudl appear only while logged on the main app page
    output = _("Your todo list")
    return HttpResponse(output)


def testing(request):
    mydata = Task.objects.all()
    template = loader.get_template('list/template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context,request))

def game(request,pk):
    mymember = Task.objects.get(id=pk)
    template = loader.get_template('list/game.html')

    hidden_text = mymember.description
    context = {
        'mymember': mymember,
        'game_var': hidden_text,
    }
    return HttpResponse(template.render(context,request))

# end of debbuging part

class CustomLoginView(LoginView):
    template_name = 'list/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'list/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    email = forms.EmailField()

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage,self).form_valid(form)

    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args,**kwargs)

class TaskList(LoginRequiredMixin,ListView):
    model = Task # req model or query set
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input
            )

        context['search_imput'] = search_input
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
 # tu jest nasz rodzynek do zamiany   

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

# class TaskUpdate(LoginRequiredMixin,View):
#     model = Task
#     success_url = reverse_lazy('tasks')
#     def get(self, request,pk):
#         task = Task.objects.get(id=pk)
#         context = {'task':task}
#         return render(request , 'list/task.html',context)

#     def post(self,request, pk):
#         task = Task.objects.get(id=pk)
#         task.body = request.POST.get('body')
#         task.save()
#         return redirect('tasks')






class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')