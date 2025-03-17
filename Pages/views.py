from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, '../templates/pages/index.html')

def about(request):
    return HttpResponse('Created by Moustafa Haydar')