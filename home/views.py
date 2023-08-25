from django.shortcuts import render
from django.http import HttpResponseNotFound

def index(request):
    return render(request, 'index.html')

def error_404(request, exception):
    return HttpResponseNotFound('error 404')