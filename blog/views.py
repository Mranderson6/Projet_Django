from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import datetime
from blog.models import Article, contact_image
from blog.forms import ContactForm, ArticleForm,ContactImForm



# view accueil ou home .
def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/HTML/structuration.html', {'derniers_articles': articles})


# view d'arcticle.
def article_T(request):
    article = Article.objects.all()

    return render(request, 'blog/HTML/tout_article.html', {'articles': article})


def view_article(request, id):
    article = get_object_or_404(Article, id=id)

    return render(request, 'blog/HTML/pas_de_solution.html', {'article': article})


# view de redirection.
def vue_redirection(request):
    return render(request, 'blog/HTML/pas_de_solution.html')


def date_actuelle(request):
    return render(request, 'blog/HTML/date.html', {'date':
                                                       datetime.now()})


def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)
    return render(request, 'blog/HTML/addition.html', locals())


def affichage_info(request):
    pseudo = "jean"
    age = 15
    texte = """le produits cartesiens
Consideraons l'exemple de la projection avec la table etudiant(nom,prenom,age) et
une seconde table utilitaires(laptop,badge,rallonge). le produit cartesien de ces deux tables
sera une nouvelle table contenant le noms des etudiants coupléaux elements de la table utilitaire
donc par l'etudiant Atangana steve 20 ans aura trois fois sont nom dans la table produit une ligne
contenant son nom son prenom son age et l'utilitaire laptop une autre ligne contenant
son nom son prenom son age et l'utilitaire badge et enfin une ligne contenant son nom son prenom son
age et l'utilitaire"""
    return render(request, 'blog/HTML/user_info.html', locals())


def test_tag(request):
    sexe = "femme"
    html = "bonjour"
    if sexe == "femme":
        html += " madame"
    else:
        html += " monsieur"
    html += '!'
    return HttpResponse(html)


def sign_in(request):
    return render(request, 'blog/HTML/Formulaire_connexion.html')


def sign_up(request):
    return render(request, 'blog/HTML/Formulaire_inscription.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            envoi = True
    else:
        form = ContactForm()
    return render(request, 'blog/HTML/contact.html', locals())


def Article_Formu(request):
    article = Article()
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance= article )
        if form.is_valid():
            form.save()

            envoi = True
    else:
            form = ArticleForm(request.POST, instance= article)
    return render(request, 'blog/HTML/creation_article.html', locals())

def nouveau_contact(request):
    sauvegarde = False

    if request.method == "POST":
        form = ContactImForm(request.POST, request.FILES)
        if form.is_valid():
            contact = contact_image()
            contact.nom = form.cleaned_data["nom"]
            contact.addresse = form.cleaned_data["addresse"]
            contact.photo = form.cleaned_data["photo"]
            contact.save()

            sauvegarde = True

    else:
        form = ContactImForm()
    return render(request, 'blog/HTML/contact_im.html', locals())

def voir_contacts(request):
    contact = contact_image.objects.all()
    return render(request, 'blog/HTML/les_contacts.html', {'contacts': contact})
