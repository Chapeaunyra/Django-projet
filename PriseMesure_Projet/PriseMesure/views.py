from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import models
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
    decors_habillage_limon = Decors_Habillage_Limon.objects.all()
    decors_parquet = Decors_Parquet.objects.all()
    decors_parquet_dalle = Decors_Parquet_Dalle.objects.all()
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
            'DecorsHabillageLimon': decors_habillage_limon,
            'DecorsParquetDalle': decors_parquet_dalle,
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
    totalMarcheRonde = request.POST['totalMarcheRonde']
    totalLimonInterieur = request.POST['totalLimonInterieur']
    totalLimonExterieur = request.POST['totalLimonExterieur']
    totalHabillageDessus = request.POST['totalHabillageDessus']
    totalDecoupeNezMarche = request.POST['totalDecoupeNezMarche']
    totalPoseParquet = request.POST['totalPoseParquet']
    totalBalustrade = request.POST['totalBalustrade']
    totalCreationContremarche = request.POST['totalCreationContremarche']
    totalDeposeAncienRevetement = request.POST['totalDeposeAncienRevetement']
    totalHabillageLimon = request.POST['totalHabillageLimon']
    totalPanneauPalier = request.POST['totalPanneauPalier']
    totalMarche = request.POST['totalMarche']
    
    
    
    
    new_devis = Devis(
        # Marches
        nombre_marches = request.POST['nombreMarche'],
        decor_marches = request.POST.get('decorMarche', False),
        # Contremarches
        nombre_contremarches = request.POST['nombreContremarche'],
        decor_contremarches = request.POST.get('decorContremarche', False),
        #Profilés aluminium
        nombre_profile_alu = request.POST['nombreProfile'],
        type_profile_alu = request.POST.get('typeProfile', False),
        #  Plinthes
        nombre_plinthes = request.POST['nombrePlinthe'],
        taille_plinthes = request.POST.get('taillePlinthe', False),
        
        # Barres de seuil
        nombre_barres_seuil = request.POST['nombreBarreSeuil'],
        type_barres_seuil = request.POST.get('typeBarreSeuil', False),
        couleur_barres_seuil = request.POST.get('couleurBarreSeuil', False),
        
        #Marches palière
        nombre_marches_paliere = request.POST['nombreMarchePaliere'],
        type_marches_paliere = request.POST.get('typeMarchePaliere', False),
        taille_marches_paliere = request.POST.get('tailleMarchePaliere', False),

        # Matériel Electrique
        marche_Eclairee = request.POST['nombreMarcheEclairee'],
        marche_Non_Eclairee = request.POST['nombreMarcheNonEclairee'],
        interrupteur = request.POST['nombreInterrupteur'],
        detecteur = request.POST['nombreDetecteur'],
        unite_commande = request.POST['nombreUniteCommande'],
        transfo_35w = request.POST['nombreTransfo35W'],
        transfo_75w = request.POST['nombreTransfo75W'],
        transfo_100w = request.POST['nombreTransfo100W'],

        # Stratifié en rouleaux
        stratifie_rouleau = request.POST['metrageStratifieRouleau'],
        # Profilé de dessus de limon
        profile_limon_l18 = request.POST['nombreL18'],
        profile_limon_l28 = request.POST['nombreL28'],
        profile_limon_l80 = request.POST['nombreL80'],
        profile_limon_l120 = request.POST['nombreL120'],

        profile_limon_u58 = request.POST['nombreU58'],
        profile_limon_u65 = request.POST['nombreU65'],
        profile_limon_u75 = request.POST['nombreU75'],
        profile_limon_u85 = request.POST['nombreU85'],

        commentaire = request.POST['commentaire'],
    )
    new_devis.save()

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

        devis = new_devis
    )
    new_client.save()

    # MARCHE RONDE
    for i in totalMarcheRonde:
        a = 1

    # LIMON INTERIEUR
    for i in totalLimonInterieur:
        a = 1

    # LIMON EXTERIEUR
    for i in totalLimonExterieur:
        a = 1

    # HABILLAGE DESSUS
    for i in totalHabillageDessus:
        a = 1

    # DECOUPE NEZ DE MARCHE
    for i in totalDecoupeNezMarche:
        a = 1

    # POSE PARQUET
    for i in totalPoseParquet:
        a = 1

    # BALUSTRADE
    for i in totalBalustrade:
        a = 1

    # CREATION CONTREMARCHE
    for i in totalCreationContremarche:
        a = 1

    # DEPOSE ANCIEN REVETEMENT
    for i in totalDeposeAncienRevetement:
        a = 1

    # HABILLAGE LIMON
    for i in totalHabillageLimon:
        a = 1

    # PANNEAU PALIER
    for i in totalPanneauPalier:
        a = 1

    # MESURE MARCHE
    for i in totalMarche:
        # If nothing was written
        type_stair = request.POST.get('formeMarche' + str(i), "Non renseigné")
        Diagonal = request.POST.get('diagonale' + str(i),"Non renseigné")
        DepthL = request.POST.get('profondeurG' + str(i),"Non renseigné")
        DepthR = request.POST.get('profondeurD' + str(i), "Non renseigné")
        RetourG = request.POST.get('retourGauche' + str(i), False)
        RetourD = request.POST.get('retourDroite' + str(i), False)
        PlintheG = request.POST.get('plintheGauche' + str(i), False)
        PlintheD = request.POST.get('plintheDroite' + str(i), False)
        ProfileArriere = request.POST.get('profileArriere' + str(i), False)

        # If something was written but not accepted by Database
        if(RetourG == "on"):
            RetourG = True
        if(RetourD == "on"):
            RetourD = True
        if(PlintheG == "on"):
            PlintheG = True
        if(PlintheD == "on"):
            PlintheD = True
        if(ProfileArriere == "on"):
            ProfileArriere = True

        # Creating the objet
    
    prise_mesure = [
        Mesure_Marches (
            type_stair = type_stair,
            Diagonal = Diagonal,
            DepthL = DepthL,
            DepthR = DepthR,
            RetourG = RetourG,
            RetourD = RetourG,
            PlintheG = RetourG,
            PlintheD = RetourG,
            ProfileArriere = ProfileArriere,

            devis = new_devis
        )
        for i in totalMarche
    ]
    mesure_marches = Mesure_Marches.objects.bulk_create(prise_mesure)
    
        # new_prise_mesure = Mesure_Marches (
        #     type_stair = type_stair,
        #     Diagonal = Diagonal,
        #     DepthL = DepthL,
        #     DepthR = DepthR,
        #     RetourG = RetourG,
        #     RetourD = RetourG,
        #     PlintheG = RetourG,
        #     PlintheD = RetourG,
        #     ProfileArriere = ProfileArriere,

        #     devis = new_devis
        # )

        # # Writting data into the database
        # new_prise_mesure.save()
        


    
    # new_marches_rondes = Marches_Ronde (
    #     # number = request.POST['nombreMarcheRonde'],
    #     # taille = request.POST['tailleMarcheRonde'],

    #     devis = new_devis
    # )
    # new_limon_interieur = Limons_Interieur(
    # #     number = request.POST['longueurLimonInterieur'],
    # #     taille = request.POST['tailleMarcheRonde'],
    # #     taille = request.POST['tailleMarcheRonde'],


    #     devis = new_devis
    # )
    # new_limon_exterieur = Limons_Exterieur(

    #     devis = new_devis
    # )
    # new_habillage_limon = Habillages_Dessus (


    #     devis = new_devis
    # )
    # new_decoupe_nez_marche = Decoupes_Nez_Marche (


    #     devis = new_devis
    # )
    # new_pose_parquet = Poses_Parquet(


    #     devis = new_devis
    # )
    # new_balustrades = Balustrades(


    #     devis = new_devis
    # )
    # new_creation_contremarche = Creations_Contremarche(


    #     devis = new_devis
    # )
    # new_depose_ancien_revetement = Deposes_Ancien_Revetement(


    #     devis = new_devis
    # )
    # new_habillage_limon = Habillages_Limon(


    #     devis = new_devis
    # )
    # new_panneau_palier = Panneaux_Palier(


    #     devis = new_devis
    # )
    
    # new_marches_rondes.save()
    # new_limon_interieur.save()
    # new_limon_exterieur.save()
    # new_habillage_limon.save()
    # new_decoupe_nez_marche.save()
    # new_pose_parquet.save()
    # new_balustrades.save()
    # new_creation_contremarche.save()
    # new_depose_ancien_revetement.save()
    # new_habillage_limon.save()
    # new_panneau_palier.save()

    


    return HttpResponseRedirect('/')

def DeleteClient(request, client_id):
    client_to_delete = Clients.objects.get(id = client_id)
    client_to_delete.delete()
    return HttpResponseRedirect('/ListeClient/')