from django.shortcuts import render
from django.http import HttpResponse
# from django import codestar

# Create your views here.
def my_blog(request):
    return HttpResponse("Hello, Blog!")