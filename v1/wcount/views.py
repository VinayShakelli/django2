from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
import operator
def home(requests):
    return HttpResponse('<h1> This is the first page</h1>')
def aboutus(requests):
    return HttpResponse('<h1>I am studying</h1>')
