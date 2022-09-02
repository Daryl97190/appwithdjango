from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listings

#Pour créer une vue, il faut déclarer une fonction avec en parametre request
def hello(request):
    bands = Band.objects.all()
    listings = Listings.objects.all()
    
    return HttpResponse(f"""
                        <h1> hELLO Django</h1>
                        <p>Mes groupes préférés sont : </p>
                        <ul>
                            <li>{bands[0].name} et {listings[0].title} </li>
                            <li>{bands[1].name} et {listings[1].title}</li>
                            <li>{bands[0].name} et {listings[2].title}</li>
                        </ul>
                        """)

def about(request):
    return HttpResponse("<h1> A propos </h1> <p>Nous adorons Django</p>")

def listings(request):
    return HttpResponse("<h1>Liste des annonces</h1> <p>Tableau d'annonce</p>")

def contact(request):
    return HttpResponse("<h1>Contact</h1> <p>List contact</p>")
