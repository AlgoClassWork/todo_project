from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm
# Create your views here.
#http://127.0.0.1:8000/ -> ozon.ru
def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, 'home.html',
    {'tasks' : tasks, 'form' : form} )

#http://127.0.0.1:8000/create/
def create_task(request):
    form = TaskForm(request.POST) 
    if form.is_valid():
        form.save()

    return redirect('home')

#http://127.0.0.1:8000/delete/1
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')

#http://127.0.0.1:8000/complete/5
def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed
    task.save()
    return redirect('home')
