from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', context= {'todos':all})


def say_hello(request):
    person = {'name': 'erfan'}
    return render(request, 'hello.html', context=person)