from utils.input_utils import demander_texte, demander_nombre, load_fichier
from univers.personnage import initialiser_personnage, afficher_personnage, modifier_argent, ajouter_objet
from univers.maison import initialiser_maisons

def lancer_chapitre_1():
    print("===== Chapitre 1 : La lettre de Poudlard =====")
    nom = demander_texte("Entrez le nom de votre personnage : ")
    prenom = demander_texte("Entrez le prénom de votre personnage : ")

    print("Définissez les attributs de votre personnage (0 à 10).")
    courage = demander_nombre("Courage : ", 0, 10)
    loyaute = demander_nombre("Loyauté : ", 0, 10)
    ambition = demander_nombre("Ambition : ", 0, 10)
    intelligence = demander_nombre("Intelligence : ", 0, 10)

    attributs = {
        "courage": courage,
        "loyaute": loyaute,
        "ambition": ambition,
        "intelligence": intelligence
    }

    joueur = initialiser_personnage(nom, prenom, attributs)
    afficher_personnage(joueur)

    print()
    print("Un hibou frappe à ta fenêtre...")
    print("Tu reçois ta lettre d'admission à l'école de sorcellerie !")
    print("Puis Hagrid arrive pour t'emmener au Chemin de Traverse acheter tes fournitures.")
    print()

    try:
        inventaire_data = load_fichier("data/inventaire.json")
    except FileNotFoundError:
        print("Fichier inventaire.json introuvable, aucun achat possible.")
        inventaire_data = []

    if isinstance(inventaire_data, dict):
        objets_disponibles = inventaire_data.get("objets", [])
    else:
        objets_disponibles = inventaire_data

    print("Tu disposes de", joueur["Argent"], "pièces d'or pour acheter du matériel.")

    terminer = False
    while not terminer and len(objets_disponibles) > 0:
        print()
        print("Objets disponibles :")
        i = 0
        while i < len(objets_disponibles):
            objet = objets_disponibles[i]
            nom_obj = objet["nom"]
            prix = objet["prix"]
            print(str(i + 1) + ".", nom_obj, "-", prix, "pièces")
            i = i + 1
        print("0. Terminer les achats")

        choix = demander_nombre("Que veux-tu acheter ? (numéro) : ", 0, len(objets_disponibles))

        if choix == 0:
            terminer = True
        else:
            index = choix - 1
            objet = objets_disponibles[index]
            nom_obj = objet["nom"]
            prix = objet["prix"]

            if joueur["Argent"] >= prix:
                modifier_argent(joueur, -prix)
                ajouter_objet(joueur, "Inventaire", nom_obj)
                print("Tu as acheté", nom_obj, ". Argent restant :", joueur["Argent"])
            else:
                print("Tu n'as pas assez d'argent pour acheter", nom_obj)

    print()
    print("Fin du chapitre 1. Tu es prêt pour le voyage vers Poudlard !")
    afficher_personnage(joueur)

    try:
        maisons_data = load_fichier("data/maisons.json")
    except FileNotFoundError:
        maisons_data = ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]

    if isinstance(maisons_data, dict):
        noms_maisons = list(maisons_data.keys())
    else:
        noms_maisons = maisons_data

    maisons = initialiser_maisons(noms_maisons)

    return joueur, maisons