from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Task
import json

# Create your views here.

def home(request):
    tasks= Task.objects.all()
    context={"tasks":tasks}
    return render(request, 'ToDoapp/home.html', context)


def createTask(request):
    task=request.POST.get('taskName', '')
    t=Task(taskName=task, complete=False)
    t.save()
    return redirect(home)


def updateTask(request):
    data=json.loads(request.body)
    taskId= data['taskId']
    action= data['action']
    
    task=Task.objects.get(id=taskId)
    
    if action=="complete":
        task.complete=True
        task.save()
    elif action=="delete":
        task.delete()
    
    
    return JsonResponse('Task updated', safe=False)