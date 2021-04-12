from django.shortcuts import render
from django.http import HttpResponse

# Create your views/ here.
def index1(request):
    return HttpResponse("<h1>hii welcome to index1</h1>")

def index2(request,name):
    return HttpResponse(f'<h1>my name is {name}</h1>')

def index3(request,gmail):
    return render(request,"sample.html",context={"gmail":gmail,"name":"sharan"})