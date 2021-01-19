from django.urls import path
from .views import todo_list_view

urlpatterns = [
    path('todo-list/', todo_list_view),
    path('todo-list/<int:list_id>/', todo_list_view)
    
]