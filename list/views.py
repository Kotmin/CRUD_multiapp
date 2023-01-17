from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def taskList(request):
    """
    Main functionality returns a HTTPresponce
    """
    return HttpResponse("todo list")