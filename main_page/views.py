from django.shortcuts import render
from django.http import HttpResponse

def index_page(request):
    return render(request, 'index.html')

#def index_page(request):
#    return HttpResponse("<h1>Главная</h1>")
