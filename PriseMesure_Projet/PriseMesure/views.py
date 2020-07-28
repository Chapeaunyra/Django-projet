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

def ClientDetailsView(request, client_id):
    client_details = Clients.objects.get(id = client_id)
    devis_details = Devis.objects.get(id = client_details.devis.id)
    prise_mesure_details = Mesure_Marches.objects.filter(devis = devis_details.id)
    marche_rondes = Marches_Ronde.objects.filter(devis = devis_details.id)
    limon_ext = Limons_Exterieur.objects.filter(devis = devis_details.id)
    limon_int = Limons_Interieur.objects.filter(devis = devis_details.id)
    habillage_dessus = Habillages_Dessus.objects.filter(devis = devis_details.id)
    decoupe_nez = Decoupes_Nez_Marche.objects.filter(devis = devis_details.id)
    pose_parquet = Poses_Parquet.objects.filter(devis = devis_details.id)
    balustrade = Balustrades.objects.filter(devis = devis_details.id)
    crea_cm = Creations_Contremarche.objects.filter(devis = devis_details.id)
    depose_ancien_revet = Deposes_Ancien_Revetement.objects.filter(devis = devis_details.id)
    habillage_limon = Habillages_Limon.objects.filter(devis = devis_details.id)
    panneau_palier = Panneaux_Palier.objects.filter(devis = devis_details.id)
    
    return render(request, 'clientDetails.html',
        {'Client':client_details,
         'Details': devis_details,
         'PriseMesure': prise_mesure_details,
         'MarcheRonde':marche_rondes,
         'LimonExt':limon_ext,
         'LimonInt':limon_int,
         'HabillageDessus':habillage_dessus,
         'DecoupeNez':decoupe_nez,
         'PoseParquet':pose_parquet,
         'Balustrade':balustrade,
         'CreationContremarche':crea_cm,
         'DeposeAncienRevet':depose_ancien_revet,
         'HabillageLimon':habillage_limon,
         'PanneauPalier':panneau_palier,
        })

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
    totalMarcheRonde = int(request.POST['totalMarcheRonde'])
    totalLimonInterieur = int(request.POST['totalLimonInterieur'])
    totalLimonExterieur = int(request.POST['totalLimonExterieur'])
    totalHabillageDessus = int(request.POST['totalHabillageDessus'])
    totalDecoupeNezMarche = int(request.POST['totalDecoupeNezMarche'])
    totalPoseParquet = int(request.POST['totalPoseParquet'])
    totalBalustrade = int(request.POST['totalBalustrade'])
    totalCreationContremarche = int(request.POST['totalCreationContremarche'])
    totalDeposeAncienRevetement = int(request.POST['totalDeposeAncienRevetement'])
    totalHabillageLimon = int(request.POST['totalHabillageLimon'])
    totalPanneauPalier = int(request.POST['totalPanneauPalier'])
    totalMarche = int(request.POST['totalMarche'])
    
    
    
    
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
    if totalMarcheRonde != 0:
        marche_ronde = [
            Marches_Ronde (
                number = request.POST.get('nombreMarcheRonde' + str(i), "1"),
                taille = request.POST.get('tailleMarcheRonde' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(totalMarcheRonde))
        ]
        Marches_Ronde.objects.bulk_create(marche_ronde)

    # LIMON INTERIEUR
    if totalLimonInterieur != 0:
        limon_interieur = [
            Limons_Interieur (
                length = request.POST.get('longueurLimonInterieur' + str(i), "0"),
                pdl = request.POST.get('PdlLimonInterieur' + str(i), "Non renseigné"),
                orientation = request.POST.get('coteLimonInterieur' + str(i), 0), # 0 pour gauche, 1 pour droite

                devis = new_devis
            )
            for i in (range(totalLimonInterieur))
        ]
        Limons_Interieur.objects.bulk_create(limon_interieur)

    # LIMON EXTERIEUR
    if totalLimonExterieur != 0:
        limon_exterieur = [
            Limons_Exterieur (
                number = request.POST.get('nombreLimonExterieur' + str(i), "0"),
                pdl = request.POST.get('PdlLimonExterieur' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(totalLimonExterieur))
        ]
        Limons_Exterieur.objects.bulk_create(limon_exterieur)

    # HABILLAGE DESSUS
    if totalHabillageDessus != 0:
        habillage_dessus = [
            Habillages_Dessus (
                number = request.POST.get('nombreHabillageDessus' + str(i), "0"),
                pdl = request.POST.get('PdlHabillageDessus' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(totalHabillageDessus))
        ]
        Habillages_Dessus.objects.bulk_create(habillage_dessus)

    # DECOUPE NEZ DE MARCHE
    if totalDecoupeNezMarche != 0:
        decoupe_nez_marche = [
            Decoupes_Nez_Marche (
                number = request.POST.get('nombreDecoupeNezMarche' + str(i), "0"),
                pdl = request.POST.get('PdlDecoupeNezMarche' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(totalDecoupeNezMarche))
        ]
        Decoupes_Nez_Marche.objects.bulk_create(decoupe_nez_marche)

    # POSE PARQUET
    if totalDecoupeNezMarche != 0:
        decoupe_nez_marche = [
            Decoupes_Nez_Marche (
                number = request.POST.get('nombreDecoupeNezMarche' + str(i), "0"),
                pdl = request.POST.get('PdlDecoupeNezMarche' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(totalDecoupeNezMarche))
        ]
        Decoupes_Nez_Marche.objects.bulk_create(decoupe_nez_marche)

    # BALUSTRADE
    if totalBalustrade != 0:
        balustrade = [
            Balustrades (
                number = request.POST.get('nombreBalustrade' + str(i), "0"),
                pdl = request.POST.get('PdlBalustrade' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(totalBalustrade))
        ]
        Balustrades.objects.bulk_create(balustrade)

    # CREATION CONTREMARCHE
    if totalCreationContremarche != 0:
        creation_contremarche = [
            Creations_Contremarche (
                number = request.POST.get('nombreCreationContremarche' + str(i), "0"),
                pdl = request.POST.get('PdlCreationContremarche' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(totalCreationContremarche))
        ]
        Creations_Contremarche.objects.bulk_create(creation_contremarche)

    # DEPOSE ANCIEN REVETEMENT
    if totalDeposeAncienRevetement != 0:
        depose_ancien_revetement = [
            Deposes_Ancien_Revetement (
                number = request.POST.get('nombreDeposeAncienRevetement' + str(i), "0"),
                pdl = request.POST.get('PdlDeposeAncienRevetement' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(totalDeposeAncienRevetement))
        ]
        Deposes_Ancien_Revetement.objects.bulk_create(depose_ancien_revetement)

    # HABILLAGE LIMON
    if totalHabillageLimon != 0:
        habillage_limon = [
            Habillages_Limon (
                number = request.POST.get('nombreHabillageLimon' + str(i), "0"),
                decor = request.POST.get('decorHabillageLimon' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(totalHabillageLimon))
        ]
        Habillages_Limon.objects.bulk_create(habillage_limon)

    # PANNEAU PALIER
    if totalPanneauPalier != 0:
        panneau_palier = [
            Panneaux_Palier (
                number = request.POST.get('nombrePanneauPalier' + str(i), "0"),
                taille = request.POST.get('taillePanneauPalier' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(totalPanneauPalier))
        ]
        Panneaux_Palier.objects.bulk_create(panneau_palier)

    # MESURE MARCHE
    if totalMarche != 0:
        prise_mesure = [
            Mesure_Marches (
                type_stair = request.POST.get('formeMarche' + str(i), "Non renseigné"),
                Diagonal = request.POST.get('diagonale' + str(i),"0"),
                DepthL = request.POST.get('profondeurG' + str(i),"0"),
                DepthR = request.POST.get('profondeurD' + str(i), "0"),
                RetourG = request.POST.get('retourGauche' + str(i), False),
                RetourD = request.POST.get('retourDroite' + str(i), False),
                PlintheG = request.POST.get('plintheGauche' + str(i), False),
                PlintheD = request.POST.get('plintheDroite' + str(i), False),
                ProfileArriere = request.POST.get('profileArriere' + str(i), False),

                devis = new_devis
            )
            for i in (range(totalMarche))
        ]
        Mesure_Marches.objects.bulk_create(prise_mesure)    

    return HttpResponseRedirect('/')

def DeleteClient(request, client_id):
    client_to_delete = Clients.objects.get(id = client_id)
    client_to_delete.delete()
    return HttpResponseRedirect('/ListeClient/')