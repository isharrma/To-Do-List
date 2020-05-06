from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.urls import reverse

from .models import Todo_list


def index(request):
    todo_items = Todo_list.objects.all().order_by('pub_date')
    return render(request, 'Todolist/index.html',
                    {
                        "todo_items": todo_items
                    })

@csrf_exempt
def add_todo(request):
    content = request.POST['content']
    date = timezone.now()
    new_obj = Todo_list.objects.create(pub_date=date, todo_text=content) 
    print(new_obj)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    Todo_list.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
