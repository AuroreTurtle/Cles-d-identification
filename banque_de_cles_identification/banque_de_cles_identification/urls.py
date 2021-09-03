"""banque_de_cles_identification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
#from application_cles_identification.views import *
from application_cles_identification.views import home
from application_cles_identification.views import displayCle
    #listeClePublique, cleUpdate
from application_cles_identification.views import taxonCreate, questionCreate, reponseCreate, cleCreate, userHome, utilisateurCreate, cleUse, displayTaxon, userConnexion

# urlpatterns=routes. 'home' est le chemin, ce que reçoit le serveur.
# hello est la fonction défini dans application_cles_identification.views, ce que retourne le serveur.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name='page_home'), # page d'accueil avec les clés publiques et l'identification
    path('cle/<int:cles_id>', displayCle, name='page_cle'), # page qui affiche une clé complète déjà créée
    #path('cle/publique', listeClePublique, name='page_cle_publique'), # page qui affiche la liste des clé publiques
    #path('cle/publique_prive', listeClePubliquePrive, name='page_cle_publique_prive'), # page qui affiche la liste de toutes les clés, publiques et privés, après identification
    path('user/home/<int:user_id>', userHome, name='page_options_utilisateur'), # page qui affiche les options de l'utilsateur comme créer un clé ou update, une fois qu'il s'est identifié
    path('cle/create', cleCreate, name='page_cle_create'),# page qui renvoi au formulaire de création d'une nouvelle clé
    path('cle/use/<int:cles_id>/<int:question_id>', cleUse, name='page_cle_utilisation'),
    path('cle/taxon/create', taxonCreate, name='page_taxon_create'), # page qui suit cle_create pour remplir tous les taxons terminaux
    path('cle/question/create', questionCreate, name='page_question_create'), # page qui suit taxon_create pour rentrer la première question
    path('cle/reponse/create', reponseCreate, name='page_reponse_create'), # page qui suit question_create pour créer les réponses liées à la questions mère et les questions filles ou les taxons
    #path('cle/update/<int:c_id>', cleUpdate, name='page_cle_update'), # page d'update de clé
    path('cle/create/user', utilisateurCreate, name= 'page_user_create'),
    path('cle/taxon/<int:cles_id>/<int:taxon_id>', displayTaxon, name='page_taxon'),
    path('user/connexion', userConnexion, name='page_user_connexion')
]
