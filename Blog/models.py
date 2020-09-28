from django.db import models
from django.urls import reverse
from django.contrib import admin


# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=30)
    auteur = models.CharField(max_length=60)
    slug = models.SlugField(max_length=100,null=True,unique= True)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.titre


class Categorie(models.Model):
    nom = models.CharField(max_length=35)

    def __str__(self):
        return self.nom


class Member(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    mot_de_passe = models.CharField(max_length=30)


class Produit(models.Model):
    nom = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nom


class Vendeur(models.Model):
    nom = models.CharField(max_length=30)
    produits = models.ManyToManyField(Produit, through='Offre')

    def __unicode__(self):
        return self.nom


class Offre(models.Model):
    prix = models.IntegerField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    vendeur = models.ForeignKey(Vendeur, on_delete=models.CASCADE)

    def __unicode__(self):
        return "{0} vendu par {1}".format(self.produit, self.vendeur)

class contact_image (models.Model):
    nom = models.CharField(max_length= 40)
    addresse = models.TextField()
    photo = models.ImageField(upload_to="Templates/blog/Media/")

    def __str__(self):
        return self.nom
