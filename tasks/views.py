from django.shortcuts import render

# Create your views here.
#http://127.0.0.1:8000/ -> ozon.ru
def home(request):
    return render(request, 'home.html')
