from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import models
from .models import *

# Méthodes d'affichage des vues
def AccueilView(request):
    return render(request, 'accueil.html')

def ListClientsView(request):
    all_clients = Clients.objects.order_by('Date_created').reverse()
    return render(request, 'listClient.html',
        {'Clients' : all_clients})

def ClientDetailsView(request, client_id):
    client_details = Clients.objects.get(id = client_id)
    devis_details = Devis.objects.get(client_id = client_id)

    prise_mesure_details = Mesure_Marches.objects.filter(devis_id = devis_details.id)
    marche_rondes = Marches_Ronde.objects.filter(devis_id = devis_details.id)
    limon_ext = Limons_Exterieur.objects.filter(devis_id = devis_details.id)
    limon_int = Limons_Interieur.objects.filter(devis_id = devis_details.id)
    habillage_dessus = Habillages_Dessus.objects.filter(devis_id = devis_details.id)
    decoupe_nez = Decoupes_Nez_Marche.objects.filter(devis_id = devis_details.id)
    pose_parquet = Poses_Parquet.objects.filter(devis_id = devis_details.id)
    balustrade = Balustrades.objects.filter(devis_id = devis_details.id)
    crea_cm = Creations_Contremarche.objects.filter(devis_id = devis_details.id)
    depose_ancien_revet = Deposes_Ancien_Revetement.objects.filter(devis_id = devis_details.id)
    habillage_limon = Habillages_Limon.objects.filter(devis_id = devis_details.id)
    panneau_palier = Panneaux_Palier.objects.filter(devis_id = devis_details.id)
    
    return render(request, 'clientDetails.html',
        {'Client': client_details,
         'Details': devis_details,
         'PriseMesure': prise_mesure_details,
         'MarcheRonde': marche_rondes,
         'LimonExt': limon_ext,
         'LimonInt': limon_int,
         'HabillageDessus': habillage_dessus,
         'DecoupeNez': decoupe_nez,
         'PoseParquet': pose_parquet,
         'Balustrade': balustrade,
         'CreationContremarche': crea_cm,
         'DeposeAncienRevet': depose_ancien_revet,
         'HabillageLimon': habillage_limon,
         'PanneauPalier': panneau_palier,
        })

def DevisView(request, client_id):
    # Informations pour les dropdowns
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

    # Informations existantes en BDD
    client_details = Clients.objects.get(id = client_id)
    devis_details = Devis.objects.get(client_id = client_id)

    prise_mesure_details = Mesure_Marches.objects.filter(devis_id = devis_details.id)
    marche_rondes = Marches_Ronde.objects.filter(devis_id = devis_details.id)
    limon_ext = Limons_Exterieur.objects.filter(devis_id = devis_details.id)
    limon_int = Limons_Interieur.objects.filter(devis_id = devis_details.id)
    habillage_dessus = Habillages_Dessus.objects.filter(devis_id = devis_details.id)
    decoupe_nez = Decoupes_Nez_Marche.objects.filter(devis_id = devis_details.id)
    pose_parquet = Poses_Parquet.objects.filter(devis_id = devis_details.id)
    balustrade = Balustrades.objects.filter(devis_id = devis_details.id)
    crea_cm = Creations_Contremarche.objects.filter(devis_id = devis_details.id)
    depose_ancien_revet = Deposes_Ancien_Revetement.objects.filter(devis_id = devis_details.id)
    habillage_limon = Habillages_Limon.objects.filter(devis_id = devis_details.id)
    panneau_palier = Panneaux_Palier.objects.filter(devis_id = devis_details.id)
    
    return render(request, 'devisDetails.html',
        {
        # Existing data
         'Client': client_details,
         'Details': devis_details,
         'PriseMesure': prise_mesure_details,
         'MarcheRonde': marche_rondes,
         'LimonExt': limon_ext,
         'LimonInt': limon_int,
         'HabillageDessus': habillage_dessus,
         'DecoupeNez': decoupe_nez,
         'PoseParquet': pose_parquet,
         'Balustrade': balustrade,
         'CreationContremarche': crea_cm,
         'DeposeAncienRevet': depose_ancien_revet,
         'HabillageLimon': habillage_limon,
         'PanneauPalier': panneau_palier,

        # Dropdows data
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


# Méthodes liées aux traitements des données

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

        Street_number_site = request.POST['street_number_site'],
        Street_site = request.POST['street_site'],
        City_site = request.POST['city_site'],
        Postal_code_site = request.POST['postal_code_site'],
    )
    new_client.save()
    
    if(request.POST.get('hauteur_limon_verifier', False) == 'on'):
        hauteur_limon_verifier = True
    else:
        hauteur_limon_verifier = False

    new_devis = Devis(
        # Marches
        nombre_marches = request.POST.get('nombreMarche', 0),
        decor_marches = request.POST.get('decorMarche', False),
        # Contremarches
        nombre_contremarches = request.POST.get('nombreContremarche', 0),
        decor_contremarches = request.POST.get('decorContremarche', False),
        #Profilés aluminium
        nombre_profile_alu = request.POST.get('nombreProfile', 0),
        type_profile_alu = request.POST.get('typeProfile', False),
        #  Plinthes
        nombre_plinthes = request.POST.get('nombrePlinthe', 0),
        taille_plinthes = request.POST.get('taillePlinthe', False),
        
        # Barres de seuil
        nombre_barres_seuil = request.POST.get('nombreBarreSeuil', 0),
        type_barres_seuil = request.POST.get('typeBarreSeuil', False),
        couleur_barres_seuil = request.POST.get('couleurBarreSeuil', False),
        
        #Marches palière
        nombre_marches_paliere = request.POST.get('nombreMarchePaliere', 0),
        type_marches_paliere = request.POST.get('typeMarchePaliere', False),
        taille_marches_paliere = request.POST.get('tailleMarchePaliere', False),

        # Matériel Electrique
        marche_Eclairee = request.POST.get('nombreMarcheEclairee', 0),
        marche_Non_Eclairee = request.POST.get('nombreMarcheNonEclairee', 0),
        interrupteur = request.POST.get('nombreInterrupteur', 0),
        detecteur = request.POST.get('nombreDetecteur', 0),
        unite_commande = request.POST.get('nombreUniteCommande', 0),
        transfo_35w = request.POST.get('nombreTransfo35W', 0),
        transfo_75w = request.POST.get('nombreTransfo75W', 0),
        transfo_100w = request.POST.get('nombreTransfo100W', 0),
        hauteur_limon_verifier = hauteur_limon_verifier,

        # Stratifié en rouleaux
        stratifie_rouleau = request.POST.get('metrageStratifieRouleau', ''),

        # Profilé de dessus de limon
        profile_limon_l18 = request.POST.get('nombreL18', 0),
        profile_limon_l28 = request.POST.get('nombreL28', 0),
        profile_limon_l80 = request.POST.get('nombreL80', 0),
        profile_limon_l120 = request.POST.get('nombreL120', 0),

        profile_limon_u58 = request.POST.get('nombreU58', 0),
        profile_limon_u65 = request.POST.get('nombreU65', 0),
        profile_limon_u75 = request.POST.get('nombreU75', 0),
        profile_limon_u85 = request.POST.get('nombreU85', 0),

        # Parquets
        metrage_parquet = request.POST.get('metrageParquet', ''),
        metrage_parquet_dalle = request.POST.get('metrageDalle', ''),
        decor_parquet_dalle = request.POST.get('decorDalle', 0),


        # Plinthes
        profile_40mm = request.POST.get('nombreProfile40', 0),
        profile_58mm = request.POST.get('nombreProfile58', 0),
        droit_58mm = request.POST.get('nombreProfileDroit58', 0),
        droit_80mm = request.POST.get('nombreProfileDroit80', 0),
        droit_blanc_80mm = request.POST.get('nombreProfileDroitBlanc80', 0),
        
        angles_exterieurs = request.POST.get('nombreAnglesExterieurs', 0),
        angles_interieurs = request.POST.get('nombreAnglesInterieurs', 0),
        nombre_module_fin = request.POST.get('nombreModuleFin', 0),


        # Isolation phonique
        rouleau = request.POST.get('nombreRouleau', 0),
        rouleau_etange = request.POST.get('nombreRouleauEtanche', 0),
        panneau = request.POST.get('nombreIsolationPanneau', 0),

        commentaire = request.POST.get('commentaire', 'Aucun commentaire.'),

        client_id = new_client,
    )
    new_devis.save()

    

    # MARCHE RONDE
    if totalMarcheRonde != 0 and request.POST['nombreMarcheRonde0'] != 0:
        marche_ronde = []
        marche_ronde += [
            Marches_Ronde (
                number = request.POST.get('nombreMarcheRonde' + str(i), "1"),
                taille = request.POST.get('tailleMarcheRonde' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(0, totalMarcheRonde + 1))
        ]
        Marches_Ronde.objects.bulk_create(marche_ronde)

    # LIMON INTERIEUR
    if totalLimonInterieur != 0 and request.POST['longueurLimonInterieur0'] != 0:
        limon_interieur = []
        limon_interieur += [
            Limons_Interieur (
                length = request.POST.get('longueurLimonInterieur' + str(i), "0"),
                pdl = request.POST.get('PdlLimonInterieur' + str(i), "Non renseigné"),
                orientation = bool(request.POST.get('coteLimonInterieur' + str(i), False)), # 0 pour gauche, 1 pour droite

                devis = new_devis
            )
            for i in (range(totalLimonInterieur))
        ]
        Limons_Interieur.objects.bulk_create(limon_interieur)

    # LIMON EXTERIEUR
    if totalLimonExterieur != 0 and request.POST['nombreLimonExterieur0'] != 0:
        limon_exterieur = []
        limon_exterieur += [
            Limons_Exterieur (
                number = request.POST.get('nombreLimonExterieur' + str(i), "0"),
                pdl = request.POST.get('PdlLimonExterieur' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(0, totalLimonExterieur + 1))
        ]
        Limons_Exterieur.objects.bulk_create(limon_exterieur)

    # HABILLAGE DESSUS
    if totalHabillageDessus != 0 and request.POST['nombreHabillageDessus0'] != 0:
        habillage_dessus = []
        habillage_dessus += [
            Habillages_Dessus (
                number = request.POST.get('nombreHabillageDessus' + str(i), "0"),
                pdl = request.POST.get('PdlHabillageDessus' + str(i), "Non renseigné"),

                devis = modif_devis
            )
            for i in (range(0, totalHabillageDessus + 1))
        ]
        Habillages_Dessus.objects.bulk_create(habillage_dessus)

    # DECOUPE NEZ DE MARCHE
    if totalDecoupeNezMarche != 0 and request.POST['nombreDecoupeNezMarche0'] != 0:
        decoupe_nez_marche = []
        decoupe_nez_marche += [
            Decoupes_Nez_Marche (
                number = request.POST.get('nombreDecoupeNezMarche' + str(i), "0"),
                pdl = request.POST.get('PdlDecoupeNezMarche' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(0, totalDecoupeNezMarche + 1))
        ]
        Decoupes_Nez_Marche.objects.bulk_create(decoupe_nez_marche)

    # POSE PARQUET
    if totalPoseParquet != 0 and request.POST['nombrePoseParquet0'] != 0:
        pose_parquet = []
        pose_parquet += [
            Poses_Parquet (
                number = request.POST.get('nombrePoseParquet' + str(i), "0"),
                pdl = request.POST.get('PdlPoseParquet' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(0, totalPoseParquet + 1))
        ]
        Poses_Parquet.objects.bulk_create(pose_parquet)

    # BALUSTRADE
    if totalBalustrade != 0 and request.POST['nombreBalustrade0'] != 0:
        balustrade = []
        balustrade += [
            Balustrades (
                number = request.POST.get('nombreBalustrade' + str(i), "0"),
                pdl = request.POST.get('PdlBalustrade' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(0, totalBalustrade + 1))
        ]
        Balustrades.objects.bulk_create(balustrade)

    # CREATION CONTREMARCHE
    if totalCreationContremarche != 0 and request.POST['nombreCreationContremarche0'] != 0:
        creation_contremarche = []
        creation_contremarche += [
            Creations_Contremarche (
                number = request.POST.get('nombreCreationContremarche' + str(i), "0"),
                pdl = request.POST.get('PdlCreationContremarche' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(0, totalCreationContremarche + 1))
        ]
        Creations_Contremarche.objects.bulk_create(creation_contremarche)

    # DEPOSE ANCIEN REVETEMENT
    if totalDeposeAncienRevetement != 0 and request.POST['nombreDeposeAncienRevetement0'] != 0:
        depose_ancien_revetement = []
        depose_ancien_revetement += [
            Deposes_Ancien_Revetement (
                number = request.POST.get('nombreDeposeAncienRevetement' + str(i), "0"),
                pdl = request.POST.get('PdlDeposeAncienRevetement' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range( 0, totalDeposeAncienRevetement + 1))
        ]
        Deposes_Ancien_Revetement.objects.bulk_create(depose_ancien_revetement)

    # HABILLAGE LIMON
    if totalHabillageLimon != 0 and request.POST['nombreHabillageLimon0'] != 0:
        habillage_limon = []
        habillage_limon += [
            Habillages_Limon (
                number = request.POST.get('nombreHabillageLimon' + str(i), "0"),
                decor = request.POST.get('decorHabillageLimon' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(0, totalHabillageLimon + 1))
        ]
        Habillages_Limon.objects.bulk_create(habillage_limon)

    # PANNEAU PALIER
    if totalPanneauPalier != 0 and request.POST['nombrePanneauPalier0'] != 0:
        panneau_palier = []
        panneau_palier += [
            Panneaux_Palier (
                number = request.POST.get('nombrePanneauPalier' + str(i), "0"),
                taille = request.POST.get('taillePanneauPalier' + str(i), "Non renseigné"),

                devis = new_devis
            )
            for i in (range(0, totalPanneauPalier+1))
        ]
        Panneaux_Palier.objects.bulk_create(panneau_palier)

    # MESURE MARCHE
    if totalMarche != 0 and int(request.POST['diagonale0']) != int(0):
        prise_mesure = []
        prise_mesure += [
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
            for i in (range(0, totalMarche+1))
        ]
        Mesure_Marches.objects.bulk_create(prise_mesure)
    return HttpResponseRedirect('/')

def ModifierDevis(request, client_id):
    # Informations des données existantes
    client_details = Clients.objects.get(id = client_id)

    devis = Devis.objects.get(client_id = client_id)

    prise_mesure_details = Mesure_Marches.objects.filter(devis_id = devis.id)
    marche_rondes = Marches_Ronde.objects.filter(devis_id = devis.id)
    limon_ext = Limons_Exterieur.objects.filter(devis_id = devis.id)
    limon_int = Limons_Interieur.objects.filter(devis_id = devis.id)
    habillage_dessus = Habillages_Dessus.objects.filter(devis_id = devis.id)
    decoupe_nez = Decoupes_Nez_Marche.objects.filter(devis_id = devis.id)
    pose_parquet = Poses_Parquet.objects.filter(devis_id = devis.id)
    balustrade = Balustrades.objects.filter(devis_id = devis.id)
    crea_cm = Creations_Contremarche.objects.filter(devis_id = devis.id)
    depose_ancien_revet = Deposes_Ancien_Revetement.objects.filter(devis_id = devis.id)
    habillage_limon = Habillages_Limon.objects.filter(devis_id = devis.id)
    panneau_palier = Panneaux_Palier.objects.filter(devis_id = devis.id)

    # Informations pour les données dynamiques rentrées
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
    




    # PARTIE CLIENT
    if( request.POST['street_number_site'] != '' ):
        street_number_site = request.POST['street_number_site']
    else:
        street_number_site = client_details.Street_number_site

    if( request.POST['street_site'] != '' ):
        street_site = request.POST['street_site']
    else:
        street_site = client_details.Street_site

    if( request.POST['city_site'] != '' ):
        city_site = request.POST['city_site']
    else:
        city_site = client_details.City_site

    if( request.POST['postal_code_site'] != '' ):
        postal_code_site = request.POST['postal_code_site']
    else:
        postal_code_site = client_details.Postal_code_site

    modif_client = Clients(
        id = client_id,
        Name = client_details.Name,
        Firstname = client_details.Firstname,

        # Contact client
        Phone = client_details.Phone,
        Smartphone = client_details.Smartphone,
        # unique=True pas établit, car un client peut revenir pour une autre maison, donc devis à nouveau renseigné.
        Email = client_details.Email,

        # Adresse Physique client
        Street_number = client_details.Street_number,
        Street = client_details.Street,
        Postal_code = client_details.Postal_code,
        City = client_details.City,

        # Adresse physique du chantier
        Street_number_site = street_number_site,
        Street_site = street_site,
        Postal_code_site = postal_code_site,
        City_site = city_site,

        # Cachet agence / Concessionnaire
        # Stamp = 

    )
    modif_client.save()



    # PARTIE DEVIS / ONE ROW INFORMATIONS
    if( int(request.POST.get('nombreMarche', 0)) != int(0)):
        nombre_marches = int(request.POST.get('nombreMarche', 0))
    else:
        nombre_marches = devis.nombre_marches

    if( request.POST.get('decorMarche', False) != False ):
        decor_marches = request.POST.get('decorMarche', False)
    else:
        decor_marches = devis.decor_marches

    if( int(request.POST.get('nombreContremarche', 0)) != int(0)):
        nombre_contremarches = int(request.POST.get('nombreContremarche', 0))
    else:
        nombre_contremarches = devis.nombre_contremarches

    if( request.POST.get('decorContremarche', False) != False ):
        decor_contremarches = request.POST.get('decorContremarche', False)
    else:
        decor_contremarches = devis.decor_contremarches

    if( int(request.POST.get('nombreProfile', 0)) != int(0)):
        nombre_profile_alu = int(request.POST.get('nombreProfile', 0))
    else:
        nombre_profile_alu = devis.nombre_profile_alu

    if( request.POST.get('typeProfile', False) != False ):
        type_profile_alu = request.POST.get('typeProfile', False)
    else:
        type_profile_alu = devis.type_profile_alu

    if( int(request.POST.get('nombrePlinthe', 0)) != int(0)):
        nombre_plinthes = int(request.POST.get('nombrePlinthe', 0))
    else:
        nombre_plinthes = devis.nombre_plinthes        

    if( request.POST.get('taillePlinthe', False) != False ):
        taille_plinthes = request.POST.get('taillePlinthe', False)
    else:
        taille_plinthes = devis.taille_plinthes

    if( int(request.POST.get('nombreBarreSeuil', 0)) != int(0)):
        nombre_barres_seuil = int(request.POST.get('nombreBarreSeuil', 0))
    else:
        nombre_barres_seuil = devis.nombre_barres_seuil

    if(  request.POST.get('typeBarreSeuil', False) != False ):
        type_barres_seuil =  request.POST.get('typeBarreSeuil', False)
    else:
        type_barres_seuil = devis.type_barres_seuil

    if( request.POST.get('couleurBarreSeuil', False) != False ):
        couleur_barres_seuil = request.POST.get('couleurBarreSeuil', False)
    else:
        couleur_barres_seuil = devis.couleur_barres_seuil

    if( int(request.POST.get('nombreMarchePaliere', 0)) != int(0)):
        nombre_marches_paliere = int(request.POST.get('nombreMarchePaliere', 0))
    else:
        nombre_marches_paliere = devis.nombre_marches_paliere

    if( request.POST.get('typeMarchePaliere', False) != False ):
        type_marches_paliere = request.POST.get('typeMarchePaliere', False)
    else:
         type_marches_paliere = devis.type_marches_paliere

    if( request.POST.get('tailleMarchePaliere', False) != False):
        taille_marches_paliere = request.POST.get('tailleMarchePaliere', False)
    else:
        taille_marches_paliere = devis.taille_marches_paliere

    if( int(request.POST.get('nombreMarcheEclairee', 0)) != int(0)):
        marche_Eclairee = int(request.POST.get('nombreMarcheEclairee', 0))
    else:
        marche_Eclairee = devis.marche_Eclairee

    if( int(request.POST.get('nombreMarcheNonEclairee', 0)) != int(0) ):
        marche_Non_Eclairee =  int(request.POST.get('nombreMarcheNonEclairee', 0))
    else:
        marche_Non_Eclairee = devis.marche_Non_Eclairee

    if( int(request.POST.get('nombreInterrupteur', 0)) != int(0)):
        interrupteur =  int(request.POST.get('nombreInterrupteur', 0))
    else:
        interrupteur =  devis.interrupteur

    if( int(request.POST.get('nombreDetecteur', 0)) != int(0)):
        detecteur =  int(request.POST.get('nombreDetecteur', 0))
    else:
        detecteur = devis.detecteur

    if( int(request.POST.get('nombreUniteCommande', 0)) != int(0)):
        unite_commande = int(request.POST.get('nombreUniteCommande', 0))
    else:
        unite_commande = devis.unite_commande

    if( int(request.POST.get('nombreTransfo35W', 0)) != int(0)):
        transfo_35w = int(request.POST.get('nombreTransfo35W', 0))
    else:
        transfo_35w = devis.transfo_35w

    if( int(request.POST.get('nombreTransfo75W', 0)) != int(0)):
        transfo_75w = int(request.POST.get('nombreTransfo75W', 0))
    else:
        transfo_75w = devis.transfo_75w

    if( int(request.POST.get('nombreTransfo100W', 0)) != int(0)):
        transfo_100w = int(request.POST.get('nombreTransfo100W', 0))
    else:
        transfo_100w = devis.transfo_100w

    # if(request.POST['HauteurLimonVerifier'] == 'off'):
    #     hauteur_limon_verifier = False
    # else:
    #     hauteur_limon_verifier = True

    if(request.POST['metrageStratifieRouleau'] != '' ):
        stratifie_rouleau = request.POST['metrageStratifieRouleau']
    else:
        stratifie_rouleau = devis.stratifie_rouleau

    if( int(request.POST.get('nombreL18', 0)) != int(0)):
        profile_limon_l18 = int(request.POST.get('nombreL18', 0))
    else:
        profile_limon_l18 = devis.profile_limon_l18

    if( int(request.POST.get('nombreL28', 0)) != int(0)):
        profile_limon_l28 = int(request.POST.get('nombreL28', 0))
    else:
        profile_limon_l28 = devis.profile_limon_l28

    if( int(request.POST.get('nombreL80', 0)) != int(0)):
        profile_limon_l80 = int(request.POST.get('nombreL80', 0))
    else:
        profile_limon_l80 = devis.profile_limon_l80

    if( int(request.POST.get('nombreL120', 0)) != int(0)):
        profile_limon_l120 = int(request.POST.get('nombreL120', 0))
    else:
        profile_limon_l120 = devis.profile_limon_l120

    if( int(request.POST.get('nombreU58', 0)) != int(0)):
        profile_limon_u58 =  int(request.POST.get('nombreU58', 0))
    else:
        profile_limon_u58 = devis.profile_limon_u58

    if( int(request.POST.get('nombreU65', 0)) != int(0)):
        profile_limon_u65 =  int(request.POST.get('nombreU65', 0))
    else:
        profile_limon_u65 = devis.profile_limon_u65

    if( int(request.POST.get('nombreU75', 0)) != int(0)):
        profile_limon_u75 =  int(request.POST.get('nombreU75', 0))
    else:
        profile_limon_u75 = devis.profile_limon_u75

    if( int(request.POST.get('nombreU85', 0)) != int(0)):
        profile_limon_u85 =  int(request.POST.get('nombreU85', 0))
    else:
        profile_limon_u85 = devis.profile_limon_u85

    if( request.POST.get('metrageParquet', '') != ''):
        metrage_parquet = request.POST.get('metrageParquet', '')
    else:
        metrage_parquet = devis.metrage_parquet

    if( request.POST.get('metrageDalle', '') != ''):
        metrage_parquet_dalle = request.POST.get('metrageDalle', '')
    else:
        metrage_parquet_dalle = devis.metrage_parquet_dalle

    if( request.POST.get('decorDalle', '') != ''):
        decor_parquet_dalle = request.POST.get('decorDalle', '')
    else:
        decor_parquet_dalle = devis.decor_parquet_dalle

    if( int(request.POST.get('nombreProfile40', 0)) != int(0)):
        profile_40mm = int(request.POST.get('nombreProfile40', 0))
    else:
        profile_40mm = devis.profile_40mm

    if( int(request.POST.get('nombreProfile58', 0)) != int(0)):
        profile_58mm = request.POST.get('nombreProfile58', int(0))
    else:
        profile_58mm = devis.profile_58mm

    if( int(request.POST.get('nombreProfileDroit58', 0)) != int(0)):
        droit_58mm = int(request.POST.get('nombreProfileDroit58', 0))
    else:
        droit_58mm = devis.droit_58mm

    if( int(request.POST.get('nombreProfileDroit80', 0)) != int(0)):
        droit_80mm = int(request.POST.get('nombreProfileDroit80', 0))
    else:
        droit_80mm = devis.droit_80mm

    if( int(request.POST.get('nombreProfileDroitBlanc80', 0)) != int(0)):
        droit_blanc_80mm = int(request.POST.get('nombreProfileDroitBlanc80', 0))
    else:
        droit_blanc_80mm = devis.droit_blanc_80mm

    if( int(request.POST.get('nombreAnglesExterieurs', 0)) != int(0)):
        angles_exterieurs = int(request.POST.get('nombreAnglesExterieurs', 0))
    else:
        angles_exterieurs = devis.angles_exterieurs

    if( int(request.POST.get('nombreAnglesInterieurs', 0)) != int(0)):
        angles_interieurs = int(request.POST.get('nombreAnglesInterieurs', 0))
    else:
        angles_interieurs = devis.angles_interieurs

    if( int(request.POST.get('nombreModuleFin', 0)) != int(0)):
        nombre_module_fin = int(request.POST.get('nombreModuleFin', 0))
    else:
        nombre_module_fin = devis.nombre_module_fin

    if( int(request.POST.get('nombreRouleau', 0)) != int(0)):
        rouleau = int(request.POST.get('nombreRouleau', 0))
    else:
        rouleau = devis.rouleau

    if( int(request.POST.get('nombreRouleauEtanche', 0)) != int(0)):
        rouleau_etange = int(request.POST.get('nombreRouleauEtanche', 0))
    else:
        rouleau_etange = devis.rouleau_etange

    if( int(request.POST.get('nombreIsolationPanneau', 0)) != int(0)):
        panneau = int(request.POST.get('nombreIsolationPanneau', 0))
    else:
        panneau = devis.panneau

    if(request.POST['commentaire'] != '' ):
        commentaire = request.POST['commentaire']
    else:
        commentaire = devis.commentaire


    modif_devis = Devis(
        # Identifiant du devis
        id = devis.id,
        # Marches
        nombre_marches = nombre_marches,
        decor_marches = decor_marches,
        # Contremarches
        nombre_contremarches = nombre_contremarches,
        decor_contremarches = decor_contremarches,
        #Profilés aluminium
        nombre_profile_alu = nombre_profile_alu,
        type_profile_alu = type_profile_alu,
        #  Plinthes
        nombre_plinthes = nombre_plinthes,
        taille_plinthes = taille_plinthes,
        
        # Barres de seuil
        nombre_barres_seuil = nombre_barres_seuil,
        type_barres_seuil = type_barres_seuil,
        couleur_barres_seuil = couleur_barres_seuil,
        
        #Marches palière
        nombre_marches_paliere = nombre_marches_paliere,
        type_marches_paliere = type_marches_paliere,
        taille_marches_paliere = taille_marches_paliere,

        # Matériel Electrique
        marche_Eclairee = marche_Eclairee,
        marche_Non_Eclairee = marche_Non_Eclairee,
        interrupteur = interrupteur,
        detecteur = detecteur,
        unite_commande = unite_commande,
        transfo_35w = transfo_35w,
        transfo_75w = transfo_75w,
        transfo_100w = transfo_100w,
        # hauteur_limon_verifier = hauteur_limon_verifier,

        # Stratifié en rouleaux
        stratifie_rouleau = stratifie_rouleau,
        # Profilé de dessus de limon
        profile_limon_l18 = profile_limon_l18,
        profile_limon_l28 = profile_limon_l28,
        profile_limon_l80 = profile_limon_l80,
        profile_limon_l120 = profile_limon_l120,

        profile_limon_u58 = profile_limon_u58,
        profile_limon_u65 = profile_limon_u65,
        profile_limon_u75 = profile_limon_u75,
        profile_limon_u85 = profile_limon_u85,

        # Parquets
        metrage_parquet = metrage_parquet,
        metrage_parquet_dalle = metrage_parquet_dalle,
        decor_parquet_dalle = decor_parquet_dalle,


        # Plinthes
        profile_40mm = profile_40mm,
        profile_58mm = profile_58mm,
        droit_58mm = droit_58mm,
        droit_80mm = droit_80mm,
        droit_blanc_80mm = droit_blanc_80mm,
        
        angles_exterieurs = angles_exterieurs,
        angles_interieurs = angles_interieurs,
        nombre_module_fin = nombre_module_fin,


        # Isolation phonique
        rouleau = rouleau,
        rouleau_etange = rouleau_etange,
        panneau = panneau,

        commentaire = commentaire,

        client_id = client_details
    )
    modif_devis.save()

    # MARCHE RONDE
    if request.POST['nombreMarcheRonde0'] != "0":
        marche_ronde = []
        marche_ronde += [
            Marches_Ronde (
                number = request.POST.get('nombreMarcheRonde' + str(i), "1"),
                taille = request.POST.get('tailleMarcheRonde' + str(i), "Non renseigné"),

                devis = modif_devis
            )
            for i in (range(0, totalMarcheRonde + 1))
        ]
        Marches_Ronde.objects.bulk_create(marche_ronde)

    # LIMON INTERIEUR
    if request.POST['longueurLimonInterieur0'] != '':
        limon_interieur = []
        limon_interieur += [
            Limons_Interieur (
                length = request.POST.get('longueurLimonInterieur' + str(i), "0"),
                pdl = request.POST.get('PdlLimonInterieur' + str(i), "Non renseigné"),
                orientation = request.POST.get('coteLimonInterieur' + str(i), "Gauche"),

                devis = modif_devis
            )
            for i in (range(0, totalLimonInterieur + 1))
        ]
        Limons_Interieur.objects.bulk_create(limon_interieur)

    # LIMON EXTERIEUR
    if request.POST['nombreLimonExterieur0'] != "0":
        limon_exterieur = []
        limon_exterieur += [
            Limons_Exterieur (
                number = request.POST.get('nombreLimonExterieur' + str(i), "0"),
                pdl = request.POST.get('PdlLimonExterieur' + str(i), "Non renseigné"),

                devis = modif_devis
            )
            for i in (range(0, totalLimonExterieur + 1))
        ]
        Limons_Exterieur.objects.bulk_create(limon_exterieur)

    # HABILLAGE DESSUS
    if request.POST['nombreHabillageDessus0'] != "0":
        habillage_dessus = []
        habillage_dessus += [
            Habillages_Dessus (
                number = request.POST.get('nombreHabillageDessus' + str(i), "0"),
                pdl = request.POST.get('PdlHabillageDessus' + str(i), "Non renseigné"),

                devis = modif_devis
            )
            for i in (range(0, totalHabillageDessus + 1))
        ]
        Habillages_Dessus.objects.bulk_create(habillage_dessus)

    # DECOUPE NEZ DE MARCHE
    if request.POST['nombreDecoupeNezMarche0'] != "0":
        decoupe_nez_marche = []
        decoupe_nez_marche += [
            Decoupes_Nez_Marche (
                number = request.POST.get('nombreDecoupeNezMarche' + str(i), "0"),
                pdl = request.POST.get('PdlDecoupeNezMarche' + str(i), "Non renseigné"),

                devis = modif_devis
            )
            for i in (range(0, totalDecoupeNezMarche + 1))
        ]
        Decoupes_Nez_Marche.objects.bulk_create(decoupe_nez_marche)

    # POSE PARQUET
    if request.POST['nombrePoseParquet0'] != "0":
        pose_parquet = []
        pose_parquet += [
            Poses_Parquet (
                number = request.POST.get('nombrePoseParquet' + str(i), "0"),
                pdl = request.POST.get('PdlPoseParquet' + str(i), "Non renseigné"),

                devis = modif_devis
            )
            for i in (range(0, totalPoseParquet + 1))
        ]
        Poses_Parquet.objects.bulk_create(pose_parquet)

    # BALUSTRADE
    if request.POST['nombreBalustrade0'] != "0":
        balustrade = []
        balustrade += [
            Balustrades (
                number = request.POST.get('nombreBalustrade' + str(i), "0"),
                pdl = request.POST.get('PdlBalustrade' + str(i), "Non renseigné"),

                devis = modif_devis
            )
            for i in (range(0, totalBalustrade + 1))
        ]
        Balustrades.objects.bulk_create(balustrade)

    # CREATION CONTREMARCHE
    if request.POST['nombreCreationContremarche0'] != "0":
        creation_contremarche = []
        creation_contremarche += [
            Creations_Contremarche (
                number = request.POST.get('nombreCreationContremarche' + str(i), "0"),
                pdl = request.POST.get('PdlCreationContremarche' + str(i), "Non renseigné"),

                devis = modif_devis
            )
            for i in (range(0, totalCreationContremarche + 1))
        ]
        Creations_Contremarche.objects.bulk_create(creation_contremarche)

    # DEPOSE ANCIEN REVETEMENT
    if request.POST['nombreDeposeAncienRevetement0'] != "0":
        depose_ancien_revetement = []
        depose_ancien_revetement += [
            Deposes_Ancien_Revetement (
                number = request.POST.get('nombreDeposeAncienRevetement' + str(i), "0"),
                pdl = request.POST.get('PdlDeposeAncienRevetement' + str(i), "Non renseigné"),

                devis = modif_devis
            )
            for i in (range( 0, totalDeposeAncienRevetement + 1))
        ]
        Deposes_Ancien_Revetement.objects.bulk_create(depose_ancien_revetement)

    # HABILLAGE LIMON
    if request.POST['nombreHabillageLimon0'] != "0":
        habillage_limon = []
        habillage_limon += [
            Habillages_Limon (
                number = request.POST.get('nombreHabillageLimon' + str(i), "0"),
                decor = request.POST.get('decorHabillageLimon' + str(i), "Non renseigné"),

                devis = modif_devis
            )
            for i in (range(0, totalHabillageLimon + 1))
        ]
        Habillages_Limon.objects.bulk_create(habillage_limon)

    # PANNEAU PALIER
    if request.POST['nombrePanneauPalier0'] != "0":
        panneau_palier = []
        panneau_palier += [
            Panneaux_Palier (
                number = request.POST.get('nombrePanneauPalier' + str(i), "0"),
                taille = request.POST.get('taillePanneauPalier' + str(i), "Non renseigné"),

                devis = modif_devis
            )
            for i in (range(0, totalPanneauPalier+1))
        ]
        Panneaux_Palier.objects.bulk_create(panneau_palier)

    # MESURE MARCHE
    if request.POST['diagonale0'] != "0":
        prise_mesure = []
        prise_mesure += [
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

                devis = modif_devis
            )
            for i in (range(0, totalMarche+1))
        ]
        Mesure_Marches.objects.bulk_create(prise_mesure)
    
    return HttpResponseRedirect('/UpdateClient/' + str(client_id) + '/')




# Méthodes de suppression d'items BDD

def DeleteClient(request, client_id):
    Clients.objects.get(id = client_id).delete()
    return HttpResponseRedirect('/ListeClient/')

def DeleteMarcheRonde(request, client_id , item_id):
    Marches_Ronde.objects.get(id = item_id).delete()
    return HttpResponseRedirect('/UpdateClient/' + str(client_id) + '/')

def DeleteLimonInterieur(request, client_id , item_id):
    Limons_Interieur.objects.get(id = item_id).delete()
    return HttpResponseRedirect('/UpdateClient/' + str(client_id) + '/')

def DeleteLimonExterieur(request, client_id , item_id):
    Limons_Exterieur.objects.get(id = item_id).delete()
    return HttpResponseRedirect('/UpdateClient/' + str(client_id) + '/')

def DeleteHabillageDessus(request, client_id , item_id):
    Habillages_Dessus.objects.get(id = item_id).delete()
    return HttpResponseRedirect('/UpdateClient/' + str(client_id) + '/')
    
def DeleteDecoupeNezMarche(request, client_id , item_id):
    Decoupes_Nez_Marche.objects.get(id = item_id).delete()
    return HttpResponseRedirect('/UpdateClient/' + str(client_id) + '/')
    
def DeletePoseParquet(request, client_id , item_id):
    Poses_Parquet.objects.get(id = item_id).delete()
    return HttpResponseRedirect('/UpdateClient/' + str(client_id) + '/')
    
def DeleteBalustrade(request, client_id , item_id):
    Balustrades.objects.get(id = item_id).delete()
    return HttpResponseRedirect('/UpdateClient/' + str(client_id) + '/')
    
def DeleteCreationContremarche(request, client_id , item_id):
    Creations_Contremarche.objects.get(id = item_id).delete()
    return HttpResponseRedirect('/UpdateClient/' + str(client_id) + '/')
    
def DeleteDeposeAncienRevetement(request, client_id , item_id):
    Deposes_Ancien_Revetement.objects.get(id = item_id).delete()
    return HttpResponseRedirect('/UpdateClient/' + str(client_id) + '/')
    
def DeleteHabillageLimon(request, client_id , item_id):
    Habillages_Limon.objects.get(id = item_id).delete()
    return HttpResponseRedirect('/UpdateClient/' + str(client_id) + '/')
    
def DeletePanneauPalier(request, client_id , item_id):
    Panneaux_Palier.objects.get(id = item_id).delete()
    return HttpResponseRedirect('/UpdateClient/' + str(client_id) + '/')
    
def DeleteMesureMarche(request, client_id , item_id):
    Mesure_Marches.objects.get(id = item_id).delete()
    return HttpResponseRedirect('/UpdateClient/' + str(client_id) + '/')



