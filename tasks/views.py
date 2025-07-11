from django.shortcuts import render

from .models import Task
# Create your views here.
#http://127.0.0.1:8000/ -> ozon.ru
def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks' : tasks})
