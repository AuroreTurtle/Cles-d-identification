from django.shortcuts import render, redirect
from application_cles_identification.models import Cles, Taxon, Question, Reponse, Utilisateur
from .forms import ClesForm, TaxonForm, QuestionForm, ReponseForm, UtilisateurForm, LogInForm

# Create your views here.
def home(request):
    liste_cles=Cles.objects.all()#On récupère la liste des clés existantes..
    liste_cles_publiques=[]#
    for i in liste_cles:#Dans la liste des clés existantes
        if i.cles_public==True:# On récupère celles qui sont publiques
            liste_cles_publiques.append(i)#et on les ajoute dans la liste des clés publiques
    return render(request, 'application_cles_identification/home.html', {'liste_cles_publiques':liste_cles_publiques})#et on renvoie cette liste pour la page Home

def cleUse(request, cles_id, question_id):
    cles = Cles.objects.get(id=cles_id)
    question = Question.objects.filter(id=question_id) # on va chercher l'objet qui correspond au id qu'on a demandé
    print(type(question))
    for i in question:
        reponse = Reponse.objects.filter(reponse_mere=i.id)
    return render(request, 'application_cles_identification/cle_use.html', {'cles':cles, 'question':question, 'reponse':reponse })
    


def userHome(request, user_id):
    try:
        utilisateur = Utilisateur.objects.get(id=user_id) # on va chercher l'objet qui correspond au id qu'on a demandé
    except:
        return render(request, 'application_cles_identification/create_nodata_url.html')

    liste_cles=Cles.objects.all()#On récupère la liste des clés existantes..
    liste_cles_publiques=[]
    liste_cles_disponibles=[]
    liste_cles_privees=[]#
    for i in liste_cles:#Dans la liste des clés existantes
        if i.cles_public==True:# On récupère celles qui sont publiques
            liste_cles_publiques.append(i)#et on les ajoute dans la liste des clés publiques
    for i in liste_cles:
        if i.cles_utilisateur_id==utilisateur.id:
            liste_cles_disponibles.append(i)
    print(liste_cles_disponibles, utilisateur.id )
    for j in liste_cles_disponibles:
            if j.cles_public==False:
                liste_cles_privees.append(j)
    return render(request, 'application_cles_identification/options_utilisateur.html', {'liste_cles_disponibles':liste_cles_disponibles, 'liste_cles_publiques':liste_cles_publiques, 'liste_cles_privees':liste_cles_privees, 'utilisateur':utilisateur})#et on renvoie cette liste pour la page Home

def displayCle(request,cles_id): # int qui contient un id
    question = Question.objects.filter(question_ref_cle=cles_id)
    try:
        cles = Cles.objects.get(id=cles_id) # on va chercher l'objet qui correspond au id qu'on a demandé
    except:
        return render(request, 'application_cles_identification/create_nodata_url.html')
    for i in question:
        if i.question_un==True:
            ID_question= i.id
    
    return render(request, 'application_cles_identification/display_cle.html', {'cles':cles, 'ID_question':ID_question})

def displayTaxon(request,cles_id, taxon_id): # int qui contient un id
    cles = Cles.objects.get(id=cles_id)
    try:
        taxon = Taxon.objects.get(id=taxon_id) # on va chercher l'objet qui correspond au id qu'on a demandé
    except:
        return render(request, 'application_cles_identification/create_nodata_url.html')

    return render(request, 'application_cles_identification/display_taxon.html', {'taxon':taxon, 'cles':cles})

def userConnexion(request):
    form = LogInForm(request.POST or None)
    if form.is_valid():
        x=form.data['utilisateur_pseudonyme']
        try:
            utilisateur=Utilisateur.objects.get(utilisateur_pseudonyme=x)
        except:
            return redirect ('page_user_create')
    return redirect ('page_options_utilisateur', user_id=utilisateur.id)


def cleCreate(request):
    cles = Cles()#On récupère une clé vide
    cles_form = ClesForm(request.POST or None, instance=cles)#On crée le formulaire
    if cles_form.is_valid():#si le formulaire est valide..
        cles_form.save()#..on le garde
        return redirect('page_taxon_create')#et on part sur la page de la clé
    return render(request, 'application_cles_identification/cle_create.html', {'cles_form': cles_form})#on exporte sur la page de création de la clé


def taxonCreate(request):
    taxon=Taxon()
    taxon_form = TaxonForm(request.POST or None, instance=taxon)#On crée le formulaire
    if taxon_form.is_valid():#si le formulaire est valide..
        taxon_form.save()#..on le garde
        return redirect('page_taxon_create')#et on retourne sur la page de création des taxons
    return render(request, 'application_cles_identification/taxon_create.html',{'taxon_form': taxon_form})#on exporte sur la page de création des taxons

def questionCreate(request):
    question=Question()#On récupère une question vide
    question_form = QuestionForm(request.POST or None, instance=question)#On crée le formulaire
    if question_form.is_valid():#si le formulaire est valide..
        question_form.save()#..on le garde
        return redirect('page_question_create')#et va sur la page de création des taxons
    return render(request, 'application_cles_identification/question_create.html',{'question_form': question_form})#on exporte sur la page de création de la première question

def reponseCreate(request):
    reponse= Reponse()#On récupère une réponse vide
    reponse_form = ReponseForm(request.POST or None, instance=reponse)#On crée le formulaire
    print('before')
    if reponse_form.is_valid():#si les formulaire sont valides...
        print('after')
        reponse_form.save()#..on garde
        return redirect('page_reponse_create')#on retourne vers la création de questions/réponses
    return render(request, 'application_cles_identification/reponse_create.html',{'reponse_form':reponse_form})#on exporte sur la page de création des Q/R


def utilisateurCreate(request):
    utilisateur=Utilisateur()#entite utilisateur vide = instance du modele
    utilisateur_form = UtilisateurForm(request.POST or None, instance=utilisateur)#construit variable formulaire, essaye de metre ce qui est dans request.post sino met rien

    if utilisateur_form.is_valid():
        utilisateur_form.save()

        return redirect('page_options_utilisateur', user_id=utilisateur.id) #il faudrait mettre une url qui nous interesse : revenir sur la page pour recreer un utilisateur, soit redirectionner vers la fiche.

    return render(request, 'application_cles_identification/utilisateur_create.html', {'utilisateur_form':utilisateur_form}) #on afiche le formulaire, on passe come variable form.
