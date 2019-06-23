from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(req):
    res = models.Posts.objects.all();
    return render(req, 'index.html')
