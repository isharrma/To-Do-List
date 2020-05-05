from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'Todolist/index.html')


def add_todo(request):
    return render(request, 'Todolist/index.html')