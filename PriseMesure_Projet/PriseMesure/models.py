from django.db import models



# Utile pour le récapitulatif dans ListeClient/{{Clients.id}}/détails/
class Devis(models.Model):
    marche_Eclairee = models.IntegerField(null=True)
    marche_Non_Eclairee = models.IntegerField(null=True)
    interrupteur = models.IntegerField(null=True)
    detecteur = models.IntegerField(null=True)
    unite_commande = models.IntegerField(null=True)
    transfo_35w = models.IntegerField(null=True)
    transfo_75w = models.IntegerField(null=True)
    transfo_100w = models.IntegerField(null=True)

    profile_arriere = models.BooleanField(default=False)

    stratifie_rouleau = models.BooleanField(null=True)

    profile_limon_l18 = models.IntegerField(null=True)
    profile_limon_l28 = models.IntegerField(null=True)
    profile_limon_l80 = models.IntegerField(null=True)
    profile_limon_l120 = models.IntegerField(null=True)

    profile_limon_u58 = models.IntegerField(null=True)
    profile_limon_u65 = models.IntegerField(null=True)
    profile_limon_u75 = models.IntegerField(null=True)
    profile_limon_u85 = models.IntegerField(null=True)

    commentaire = models.TextField(null=True)




# PARTIE CLIENT
class Clients(models.Model):
    # Identité client
    Name = models.TextField(null=True)
    Firstname = models.TextField(null=True)

    # Contact client
    Phone = models.TextField(null=True)
    Smartphone = models.TextField()
    # unique=True pas établit, car un client peut revenir pour une autre maison, donc devis à nouveau renseigné.
    Email = models.EmailField(null=True)

    # Adresse Physique client
    Street_number = models.TextField(null=True)
    Street = models.TextField(null=True)
    Postal_code = models.TextField(null=True)
    City = models.TextField(null=True)

    # Cachet agence / Concessionnaire
    Stamp = models.ImageField(null=True)
    Date_created = models.DateField(auto_now=True)

    devis_id = models.ForeignKey(Devis, on_delete=models.PROTECT)

class Photos(models.Model):
    # Photos prise chez les clients
    photo = models.ImageField(null=True)
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)




# PARTIE PRISE DE MESURE
class Marches(models.Model):
    number = models.IntegerField(null=True)
    decor = models.TextField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Mesure_Marches(models.Model):
    # Informations de base
    type_stair = models.TextField(null=True)
    Diagonal = models.TextField(null=True)
    DepthL = models.TextField(null=True)
    DepthR = models.TextField(null=True)

    # Options
    RetourG = models.BooleanField(null=True)
    RetourD = models.BooleanField(null=True)
    PlintheG = models.BooleanField(null=True)
    PlintheD = models.BooleanField(null=True)

    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Contremarches(models.Model):
    number = models.IntegerField(null=True)
    decor = models.TextField(null=True)

    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Profiles(models.Model):
    number = models.IntegerField(null=True)
    typeProfile = models.TextField(null=True)

    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Plinthes(models.Model):
    number = models.IntegerField(null=True)
    typeProfile = models.TextField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Barres_Seuil(models.Model):
    number = models.IntegerField(null=True)
    taille = models.TextField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Marches_Paliere(models.Model):
    number = models.IntegerField(null=True)
    typeMarchePaliere = models.TextField(null=True)
    decor = models.TextField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Marches_Ronde(models.Model):
    number = models.IntegerField(null=True)
    taille = models.TextField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Limons_Interieur(models.Model):
    length = models.TextField(null=True)
    pdl = models.TextField(null=True)
    orientation = models.BooleanField() # 0 pour gauche, 1 pour droite
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Limons_Exterieur(models.Model):
    number = models.IntegerField(null=True)
    pdl = models.TextField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Habillages_Dessus(models.Model):
    number = models.IntegerField(null=True)
    pdl = models.TextField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Decoupes_Nez_Marche(models.Model):
    number = models.IntegerField(null=True)
    pdl = models.TextField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Poses_Parquet(models.Model):
    number = models.IntegerField(null=True)
    pdl = models.TextField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Balustrades(models.Model):
    number = models.IntegerField(null=True)
    pdl = models.TextField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Creations_Contremarche(models.Model):
    number = models.IntegerField(null=True)
    pdl = models.TextField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Deposes_Ancien_Revetement(models.Model):
    number = models.IntegerField(null=True)
    pdl = models.TextField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Habillages_Limon(models.Model):
    number = models.IntegerField(null=True)
    decor = models.TextField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Panneaux_Palier(models.Model):
    number = models.IntegerField(null=True)
    taille = models.TextField(null=True)

    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Parquets(models.Model):
    metrage = models.TextField(null=True)
    dalle_decor = models.TextField(null=True)
    dalle_metrage = models.TextField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Plinthes_Profile(models.Model):
    profile_40mm = models.IntegerField(null=True)
    profile_58mm = models.IntegerField(null=True)
    droit_58mm = models.IntegerField(null=True)
    droit_80mm = models.IntegerField(null=True)
    droit_blanc_80mm = models.IntegerField(null=True)
    
    angles_exterieurs = models.IntegerField(null=True)
    angles_interieurs = models.IntegerField(null=True)
    nombre_module_fin = models.IntegerField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)

class Isolations(models.Model):
    rouleau = models.IntegerField(null=True)
    rouleau_etange = models.IntegerField(null=True)
    panneau = models.IntegerField(null=True)
    
    devis_id = models.ForeignKey(Devis, on_delete=models.CASCADE)


    
    
    
    
    
    
    
    
    
    
    
    
    







# PARTIE FORMULAIRE DE PRISE DE MESURE
# Décors pour certains produits
class Decors_Marche(models.Model):
    name = models.TextField()

class Decors_Contremarche(models.Model):
    name = models.TextField()

class Decors_Parquet(models.Model):
    name = models.TextField()

class Decors_Limon(models.Model):
    name = models.TextField()

class Couleur_Bar_Seuil(models.Model):
    name = models.TextField()


# Type pour certains produits
class Types_Marche(models.Model):
    name = models.TextField()
    description = models.TextField()

class Types_Marche_Paliere(models.Model):
    name = models.TextField()
    description = models.TextField()

class Types_Profile(models.Model):
    name = models.TextField()
    description = models.TextField()

class Types_Bar_Seuil(models.Model):
    name = models.TextField()
    description = models.TextField()

# Taille pour certains produits
class Tailles_Marche_Paliere(models.Model):
    size = models.TextField()

class Tailles_Panneau(models.Model):
    size = models.TextField()

class Tailles_Plinthes(models.Model):
    size = models.TextField()