from django.urls import path
from .views import TaskList


urlpatterns = [
    path('',TaskList.as_view(), name='tasks'), # depends on used place throws __get__ / __post__ method
]