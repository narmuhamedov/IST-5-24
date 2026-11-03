from django.shortcuts import render,redirect, get_object_or_404
from todo.forms import TodoForm
from todo.models import Todo
from django.http import HttpResponse

#CRUD - create read update delete
def create_todo_view(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo_list/')
    else:
        form = TodoForm()
    return render(request, 'todo/create_todo.html', {'form': form})

def read_todo_view(request):
    if request.method == "GET":
        todo = Todo.objects.all().order_by("-id")
    return render(request, 'todo/todo_list.html', {'todo': todo})

def update_todo_view(request, id):
    todo_id = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo_id)
        if form.is_valid():
            form.save()
            return redirect('/todo_list/')
    else:
        form = TodoForm(instance=todo_id)
    return render(request, 'todo/update_todo.html', {'form': form, 'todo_id':todo_id})

def delete_todo_view(request, id):
    todo_id = get_object_or_404(Todo, id=id)
    todo_id.delete()
    return HttpResponse('<h1>Вы успешно удалили <a href="/todo_list/">На список задач</a> </h1>')