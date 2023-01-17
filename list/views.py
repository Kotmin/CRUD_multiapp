from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

# Create your views here.


def taskList(request):
    """
    Main functionality returns a HTTPresponce
    """
    # Translators: This message shoudl appear only while logged on the main app page
    output = _("Your todo list")
    return HttpResponse(output)