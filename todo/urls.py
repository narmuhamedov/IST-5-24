from django.urls import path
from todo.views import create_todo_view, read_todo_view, update_todo_view,delete_todo_view

urlpatterns = [
    path('create_todo/', create_todo_view, name='create'),
    path('todo_list/', read_todo_view, name='read'),
    path('todo_list/<int:id>/update/', update_todo_view, name='update'),
    path('todo_list/<int:id>/delete/', delete_todo_view, name='delete'),
]