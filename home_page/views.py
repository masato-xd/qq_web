# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def index(request):
#     return HttpResponse(u"球球大作战工具链接")

def index(request):
    return render(request, 'home_page/home.html')

def zqxt(request):
    string = u"我在自强学堂学习Django,建网站"
    return render(request, 'home_page/zqxt.html',{'string': string})
 
def add(request):
#    a = request.GET['a']
    a = request.GET.get('a', 0)
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
