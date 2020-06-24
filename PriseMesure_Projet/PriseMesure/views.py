from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
def AccueilView(request):
    return render(request, 'accueil.html')

def ListClientsView(request):
    all_clients = Clients.objects.order_by('Date_created')
    return render(request, 'listClient.html',
        {'Clients' : all_clients})

def PriseMesure(request):
    decors_marches = Decors_Marche.objects.all()
    decors_contremarches = Decors_Contremarche.objects.all()
    decors_limon = Decors_Limon.objects.all()
    decors_parquet = Decors_Parquet.objects.all()
    couleur_bs = Couleur_Bar_Seuil.objects.all()

    type_marche = Types_Marche.objects.all()
    type_mp = Types_Marche_Paliere.objects.all()
    type_profile = Types_Profile.objects.all()
    type_bs = Types_Bar_Seuil.objects.all()

    taille_mp = Tailles_Marche_Paliere.objects.all()
    taille_panneau = Tailles_Panneau.objects.all()
    tailles_plinthes = Tailles_Plinthes.objects.all()


    return render(request, 'priseMesure.html',
        {
            'DecorsMarche': decors_marches,
            'DecorsContremarche': decors_contremarches,
            'DecorsLimon': decors_limon,
            'DecorsParquet': decors_parquet,
            'DecorBarSeuil': couleur_bs,
            'TypesMarche': type_marche,
            'TypesMarchePaliere': type_mp,
            'TypesProfile': type_profile,
            'TypesBarSeuil': type_bs,
            'TaillesMarchePaliere': taille_mp,
            'TaillesPanneau': taille_panneau,
            'TaillesPlinthe': tailles_plinthes,
        })

def NouveauDevis(request):
    new_devis = Devis(
        marche_Eclairee = request.POST['nombreMarcheEclairee'],
        marche_Non_Eclairee = request.POST['nombreMarcheNonEclairee'],
        interrupteur = request.POST['nombreInterrupteur'],
        detecteur = request.POST['nombreDetecteur'],
        unite_commande = request.POST['nombreUniteCommande'],
        transfo_35w = request.POST['nombreTransfo35W'],
        transfo_75w = request.POST['nombreTransfo75W'],
        transfo_100w = request.POST['nombreTransfo100W'],

        profile_arriere = request.POST['profileArriere1'],

        stratifie_rouleau = request.POST['metrageStratifieRouleau'],

        profile_limon_l18 = request.POST['nombreL18'],
        profile_limon_l28 = request.POST['nombreL28'],
        profile_limon_l80 = request.POST['nombreL80'],
        profile_limon_l120 = request.POST['nombreL120'],

        profile_limon_u58 = request.POST['nombreU58'],
        profile_limon_u65 = request.POST['nombreU65'],
        profile_limon_u75 = request.POST['nombreU75'],
        profile_limon_u85 = request.POST['nombreU85'],
    )

    new_client = Clients(
        Name = request.POST['name'],
        Firstname = request.POST['firstname'],
        Street_number = request.POST['street_number'],
        Street = request.POST['street'],
        City = request.POST['city'],
        Postal_code = request.POST['postal_code'],
        Phone = request.POST['phone'],
        Smartphone = request.POST['smartphone'],
        Email = request.POST['email'],

        Id_devis = new_devis
    )
    new_devis.save()
    new_client.save()

    return HttpResponseRedirect('/')

    





















    new_client.save()
    return HttpResponseRedirect('/PriseMesure/')

def DeleteClient(request, client_id):
    client_to_delete = Clients.objects.get(id = client_id)
    client_to_delete.delete()
    return HttpResponseRedirect('/ListeClient/')