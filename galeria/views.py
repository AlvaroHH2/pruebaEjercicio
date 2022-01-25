from django.shortcuts import render

from django.http import HttpResponse
import urllib
def index(request):
    
    return HttpResponse("<h3>Hello, world. You're at the polls index.</h3> <img src='https://w7.pngwing.com/pngs/377/570/png-transparent-tree-mangifera-indica-great-tree.png'>")
# Create your views here.
