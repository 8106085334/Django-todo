from django.http import HttpResponse
from django.shortcuts import render
from todos.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks':tasks
    }
    return render(request,'index.html',context)