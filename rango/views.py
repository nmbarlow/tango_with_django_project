# from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rango import views
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Rango says hey there partner! <a href='/rango/about'>About</a>")

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about (request):
    context_dict = {'djangomessage' : "This tutorial has been put together by Nadya Barlow."}
    # return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
    return render(request, 'rango/about.html', context=context_dict)
