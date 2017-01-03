# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def index(request):
#     return HttpResponse(u"球球大作战工具链接")

def index(request):
    return render(request, 'home.html')

 
def add(request):
#    a = request.GET['a']
    a = request.GET.get('a', 0)
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
