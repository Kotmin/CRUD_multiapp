from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate


urlpatterns = [
    path('',TaskList.as_view(), name='tasks'), # depends on used place throws __get__ / __post__ method
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('task-create/',TaskCreate.as_view(), name='task-create'),
]