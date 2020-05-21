from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import todoItem
# Create your views here.

def index(request, username):
    all_todo_items = todoItem.objects.filter(user_id = username)
    return render(request, 'todo_main.html', {'all_items' : all_todo_items, 'username' : username})

def addTodo(request, username):
    _content = request.POST['content']
    userid = username
    new_item = todoItem(content = _content, user_id = username)
    new_item.save()
    return HttpResponseRedirect('/todo/{{username}}')
    
def deleteTodo(request, todo_id):
    to_delete = todoItem.objects.get(id=todo_id)
    to_delete.delete()
    return HttpResponseRedirect('/todo/{{username}}')



