#Importation des donnees pour la creation du formulaire
from django import forms
from application_cles_identification.models import *


#Formulaire pour les utilisateurs, on prend tous les champs de la table Utilisateur
class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = '__all__'


#Formulaire pour les cles, on prend tous les champs de la table Cles
class ClesForm(forms.ModelForm):
    class Meta:
        model = Cles
        fields = '__all__'


#Formulaire pour les questions, on recupere l'intitule et le detail de la table Question
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_intitule','question_detail','question_ref_cle','question_un']


#Formulaire pour les reponses, on recupere l'intitule de la reponse, la question fille (reponse_fille), le taxon terminal et la photo (optionel) dans la table Reponse
class ReponseForm(forms.ModelForm):
    reponse_taxon=forms.ModelChoiceField(required=False, queryset=Taxon.objects)
    reponse_fille=forms.ModelChoiceField(required=False, queryset=Question.objects)
    class Meta:
        model = Reponse
        fields = ['reponse_mere','reponse_intitule','reponse_fille','reponse_taxon', 'reponse_photo', 'reponse_detail', 'reponse_end']


#Formulaire pour les items terminaux, on prend tous les champs de la table Taxon
class TaxonForm(forms.ModelForm):
    class Meta:
        model = Taxon
        fields = '__all__'

#Formulaire pour les utilisateurs, on prend tous les champs de la table Utilisateur
class LogInForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['utilisateur_pseudonyme']

