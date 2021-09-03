#importation de packages
from django.db import models
from datetime import datetime

# Creation des tables/classes

class Utilisateur(models.Model):
    #id= django produit automatiquement
    utilisateur_nom = models.CharField(max_length=100, null=False)#nom d'utilisateur obligatoire
    utilisateur_prenom = models.CharField(max_length=100, null=False)#prenom d'utilisateur obligatoire
    utilisateur_pseudonyme = models.CharField(max_length=100, unique=True, null=False)#pseudonyme unique, obligatoire
    utilisateur_email = models.EmailField(max_length=70, unique=True, null=True) # email unique, pas obligatoire.
    utilisateur_date_inscription = models.DateTimeField(default=datetime.now, verbose_name="Date d'inscription")# date d'inscription de l'utilisateur sur le site.

    class Meta: #definit les metadonnees de la classe
        verbose_name = "Utilisateur" #definit <prenom> de la classe
        ordering = ['utilisateur_nom'] # pour ordener les instances de cette classe en utilisant le nom de l'utilisateur.

    def __str__(self): # quand on fait un print d'une instance il m'afiche son pseudonyme
        return self.utilisateur_pseudonyme #question

class Cles (models.Model):
    #id= django produit automatiquement
    cles_nom = models.CharField(max_length=100, null=False)# nom de la cle d'identification, c'est obligatoire
    cles_description = models.TextField (null=False) #Description en texte de la cle d'identification, c'est obligatoire
    cles_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=False) # Obligatoire. Cle etrangere referent a l'utilisateur, c'est l'utilisteur qui a cree la cle.
    cles_categorie = models.IntegerField(choices=[(1, ("Zoologie")),(2, ("Botanique")),(3, ("Géologie")),(4, ("Minéralogie")),(5, ("Autre"))],default=1)#Categorie de la cle dans notre liste deroulante (pre-definit), obligatoire.  cles_date_creation = models.DateTimeField(default=datetime.now, verbose_name="Date de création") # date de creation de la cle.
    cles_public= models.BooleanField (default=True) #La cle est publique par default, mais c'est possible dans le moment de sa creation de la changer a prive.

    class Meta:
        verbose_name = "Cles"
        ordering = ['cles_nom']

    def __str__(self):
        return self.cles_nom

class Question (models.Model):
    #id= django produit automatiquement
    question_intitule = models.CharField(max_length=1000)#C'est le texte de la question, c'est obligatoire.
    question_ref_cle = models.ForeignKey(Cles, on_delete=models.CASCADE, null=False)# Cle etrangere referent a la cle auquel cette question appartien.
    question_detail = models.CharField(max_length=1000, null=True)#champ de texte extra pour la description de la reponse, pas obligatoire
    question_un =  models.BooleanField (default=False) #Une question est la première =True quand elle a ete utilisé, ça veut dire associé à des reponses directes. On ne peut pas revenir sur une question qui a deja ete utilise.

    class Meta:
        verbose_name = "Question"
        ordering = ['question_intitule']

    def __str__(self):
        return self.question_intitule

class Taxon (models.Model):
    #id= django produit automatiquement
    taxon_nom = models.CharField(max_length=100, null=False)#nom du taxon. C'est obligatoire.
    taxon_description = models.TextField (null=False)#description du taxon, obligatoire.
    taxon_nom_scientifique = models.CharField(max_length=100, null=True)# pas obligatoire.
    taxon_photo = models.CharField(max_length=500, null=True) # photo descriptive du taxon.

    class Meta:
        verbose_name = "Taxon"
        ordering = ['taxon_nom']

    def __str__(self):
        return self.taxon_nom


class Reponse (models.Model):
    #id= django produit automatiquement
    reponse_intitule = models.CharField(max_length=1000)
    reponse_mere = models.ForeignKey(Question, related_name="reponse_origine", on_delete=models.CASCADE, null=False) #Cle etrangere referent a la question d'origine, la question source.
    reponse_fille = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="reponse", unique=True, null=True) #Cle etrangere referent a la question suivante, la question fille.
    reponse_taxon = models.ForeignKey(Taxon, on_delete=models.CASCADE, null=True) # Cle etrangere referent au taxon. La reponse peut mener a un taxon.
    reponse_photo = models.CharField(max_length=500, null=True) # photo descriptive de la reponse.
    reponse_detail = models.CharField(max_length=1000, null=True)#champs de texte extra pour la description de la reponse, pas obligatoire.
    reponse_end = models.BooleanField (default=False) #On utilise ce boolean pour signaliser quand une reponse a atteind son but : le taxon. Si end= false, elle ne renvoie pas a un taxon, elle renvoie a une question. Seule les reponses qui renvoient a un taxon ont reponse_end==True.

    class Meta:
        verbose_name = "Reponse"
        ordering = ['reponse_intitule']

    def __str__(self):
        return self.reponse_intitule
