from django.shortcuts import render
from django.http import HttpResponse

#Pour créer une vue, il faut déclarer une fonction avec en parametre request
def hello(request):
    return HttpResponse("<h1> hELLO Django</h1>")
