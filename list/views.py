from django.shortcuts import render
from django.http import HttpResponse # just for debug purposes


from django.views.generic.list import ListView
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


class TaskList(ListView):
    model = Task
    # req model or qury set