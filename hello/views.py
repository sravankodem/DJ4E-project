from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
   return render(request,"home.html",{'name':'Sravan'})

def add(request):
   #  v1 = int(request.GET.get("num1"))
   #  v2 = int(request.GET.get("num2"))
   #  res = int(v1 + v2)
   v1=int(request.POST.get('num1'))
   v2=int(request.POST.get('num2'))
   v3=int(v1+v2)
   return render(request,"result.html",{'result': v3})
