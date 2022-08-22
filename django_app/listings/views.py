from django.shortcuts import render
from django.http import HttpResponse

#Pour créer une vue, il faut déclarer une fonction avec en parametre request
def hello(request):
    return HttpResponse("<h1> hELLO Django</h1>")

def about(request):
    return HttpResponse("<h1> A propos </h1> <p>Nous adorons Django</p>")

def listings(request):
    return HttpResponse("<h1>Liste des annonces</h1> <p>Tableau d'annonce</p>")

def contact(request):
    return HttpResponse("<h1>Contact</h1> <p>List contact</p>")
