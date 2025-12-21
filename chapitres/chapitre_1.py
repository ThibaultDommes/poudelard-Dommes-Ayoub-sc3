from utils.input_utils import *
from univers.personnage import *
from univers.maison import *

def introduction():
    print("Bienvenue dans le monde magique de Poudlard.")
    print("Votre aventure commence aujourd'hui.")
    print("Une lettre très particulière va bientôt changer votre destin...")
    input("Appuyez sur Entrée pour continuer.")

def creer_personnage():
    nom = demander_texte("Entrez le nom de votre personnage : ")
    prenom = demander_texte("Entrez le prénom de votre personnage : ")

    print("Choisissez vos attributs :")
    courage = demander_nombre("Niveau de courage : ",1,10)
    intelligence = demander_nombre("Niveau d’intelligence : ",1,10)
    loyaute = demander_nombre("Niveau de loyauté : ",1,10)
    ambition = demander_nombre("Niveau d’ambition  : ",1,10)

    attributs = {
        "courage": courage,
        "intelligence": intelligence,
        "loyauté": loyaute,
        "ambition": ambition
    }

    personnage = initialiser_personnage(nom, prenom, attributs)

    print("Profil du personnage :")
    print("Nom :", personnage["Nom"])
    print("Prenom :", personnage["Prenom"])
    print("Argent :", personnage["Argent"])

    print("Inventaire :")
    print(personnage["Inventaire"])

    print("Sortilèges :")
    print(personnage["Sortilèges"])

    print("Attributs :")
    for cle, valeur in personnage["Attributs"].items():
        print("-", cle, ":", valeur)

    return personnage
