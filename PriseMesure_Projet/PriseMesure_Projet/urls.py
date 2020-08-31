"""PriseMesure_Projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from PriseMesure.views import (
    # Views
    AccueilView, 
    ListClientsView, 
    DevisView, 
    ClientDetailsView,

    # Traitements de données
    PriseMesure, 
    NouveauDevis, 
    ModifierDevis, 

    # Suppression de données
    DeleteClient, 
    DeleteMarcheRonde, 
    DeleteLimonInterieur,
    DeleteLimonExterieur, 
    DeleteHabillageDessus, 
    DeleteDecoupeNezMarche, 
    DeletePoseParquet,
    DeleteBalustrade,
    DeleteCreationContremarche,
    DeleteDeposeAncienRevetement,
    DeleteHabillageLimon,
    DeletePanneauPalier,
    DeleteMesureMarche
    )

urlpatterns = [
    # Partie ADMIN (non utilisé actuellement)
    path('admin/', admin.site.urls),

    # Views
    path('', AccueilView),
    path('ListeClient/', ListClientsView),
    path('ListeClient/<int:client_id>/', ClientDetailsView),
    path('UpdateClient/<int:client_id>/', DevisView),


    # Traitements des données
    path('PriseMesure/', PriseMesure),
    path('NouveauDevis/', NouveauDevis),
    path('ModifierDevis/<int:client_id>/', ModifierDevis),


    # Suppression de données
    path('DeleteClient/<int:client_id>/', DeleteClient),
    path('DeleteMarcheRonde/<int:client_id>/<int:item_id>', DeleteMarcheRonde),
    path('DeleteLimonInterieur/<int:client_id>/<int:item_id>', DeleteLimonInterieur),
    path('DeleteLimonExterieur/<int:client_id>/<int:item_id>', DeleteLimonExterieur),
    path('DeleteHabillageDessus/<int:client_id>/<int:item_id>', DeleteHabillageDessus),
    path('DeleteDecoupeNezMarche/<int:client_id>/<int:item_id>', DeleteDecoupeNezMarche),
    path('DeletePoseParquet/<int:client_id>/<int:item_id>', DeletePoseParquet),
    path('DeleteBalustrade/<int:client_id>/<int:item_id>', DeleteBalustrade),
    path('DeleteCreationContremarche/<int:client_id>/<int:item_id>', DeleteCreationContremarche),
    path('DeleteDeposeAncienRevetement/<int:client_id>/<int:item_id>', DeleteDeposeAncienRevetement),
    path('DeleteHabillageLimon/<int:client_id>/<int:item_id>', DeleteHabillageLimon),
    path('DeletePanneauPalier/<int:client_id>/<int:item_id>', DeletePanneauPalier),
    path('DeleteMesureMarche/<int:client_id>/<int:item_id>', DeleteMesureMarche),
]