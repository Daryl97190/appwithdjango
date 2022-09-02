from django.db import models

class Band(models.Model):
    
    # Champ qui stocke les données de type chaine/caractère/texte dans une base de données
    name = models.fields.CharField(max_length=100)

class Listings(models.Model):
    title = models.fields.CharField(max_length=100)