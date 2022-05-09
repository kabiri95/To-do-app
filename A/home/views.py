from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', context= {'todos':all})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo':todo})

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('home')
