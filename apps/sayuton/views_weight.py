from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request, id):
    return HttpResponse(f'hello index {id}')


def list(request):
    return HttpResponse('hello world')


def add(request):
    return HttpResponse('hello world')


def delete(request):
    return HttpResponse('hello world')


def update(request):
    return HttpResponse('hello world update')
