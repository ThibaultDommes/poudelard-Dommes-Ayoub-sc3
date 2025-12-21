from utils.input_utils import *
from univers.personnage import *
from univers.maison import *
import sys
import json
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
        "loyaute": loyaute,
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
def recevoir_lettre():
    print("Une lettre arrive par hibou...")
    print("Cher(e) élève, vous êtes accepté(e) à Poudlard !")
    print("Souhaitez-vous accepter cette invitation ?")

    # Utilisation de demander_choix pour proposer les deux options
    choix = demander_choix("Que décidez-vous ?", ["Oui, j'accepte", "Non, je refuse"])

    if choix == 2:
        print("Vous avez refusé l'aventure. Dommage ! Le hibou s'envole avec votre lettre...")
        sys.exit(0)  # Arrêt immédiat du programme
    else:
        print("Vous acceptez l'invitation ! L'aventure commence !")

def rencontrer_hagrid(personnage):
    print("Hagrid : Salut " + personnage["Prenom"] + "! Je suis venu t’aider à faire vos achats sur le Chemin de Traverse.")
    print("Voulez-vous suivre Hagrid ?")

    # Proposer les deux options
    choix = demander_choix("Votre choix :", ["Oui", "Non"])

    if choix == 1:
        print(f"Vous décidez de suivre Hagrid. Il vous entraîne vers le Chemin de Traverse !")
    else:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui !")
import json
import sys

import sys

def acheter_fournitures(personnage):
    print("Bienvenue sur le Chemin de Traverse !")

    # Catalogue interne (liste de dictionnaires)
    catalogue = [
        {"nom": "Baguette magique", "prix": 35},
        {"nom": "Robe de sorcier", "prix": 20},
        {"nom": "Chaudron en étain", "prix": 15},
        {"nom": "Manuel de potions", "prix": 25},
        {"nom": "Plume magique", "prix": 5},
        {"nom": "Livre enchanté", "prix": 30},
        {"nom": "Balance de cuivre", "prix": 10},
        {"nom": "Cape d'invisibilité", "prix": 100}
    ]

    # Objets obligatoires
    obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]

    # Inventaire temporaire
    inventaire = []

    # Argent initial
    argent = personnage["Argent"]

    # Achat des objets obligatoires
    while len(obligatoires) > 0:
        print("\nCatalogue des objets disponibles :")
        for i in range(len(catalogue)):
            print(str(i+1) + ". " + catalogue[i]["nom"] + " - " + str(catalogue[i]["prix"]) + " galions")

        print("\nVous avez " + str(argent) + " galions.")
        print("Objets obligatoires restant à acheter : " + ", ".join(obligatoires))

        choix = demander_nombre("Entrez le numéro de l'objet à acheter", 1, len(catalogue))
        produit = catalogue[choix - 1]

        if argent < produit["prix"]:
            print("Vous n'avez pas assez d'argent pour acheter cet objet.")
        else:
            inventaire.append(produit["nom"])
            argent -= produit["prix"]
            print("Vous avez acheté : " + produit["nom"] + " (-" + str(produit["prix"]) + " galions).")
            print("Vous avez " + str(argent) + " galions.")

            if produit["nom"] in obligatoires:
                obligatoires.remove(produit["nom"])

    print("\nTous les objets obligatoires ont été achetés !")
    animaux = [
        {"nom": "Chouette", "prix": 20},
        {"nom": "Chat", "prix": 15},
        {"nom": "Rat", "prix": 10},
        {"nom": "Crapaud", "prix": 5}
    ]

    print("\nIl est temps de choisir votre animal de compagnie pour Poudlard !")
    print("Vous avez " + str(argent) + " galions.")
    print("Voici les animaux disponibles :")
    for i in range(len(animaux)):
        print(str(i+1) + ". " + animaux[i]["nom"] + " - " + str(animaux[i]["prix"]) + " galions")

    choix_animal = demander_nombre("Quel animal voulez-vous ?", 1, len(animaux))
    animal_choisi = animaux[choix_animal - 1]

    if argent < animal_choisi["prix"]:
        print("Vous n'avez pas assez d'argent pour cet animal. Le jeu est terminé.")
        sys.exit(0)

    inventaire.append(animal_choisi["nom"])
    argent -= animal_choisi["prix"]
    print("Vous avez choisi : " + animal_choisi["nom"] + " (-" + str(animal_choisi["prix"]) + " galions).")

    personnage["argent"] = argent
    personnage["inventaire"] = inventaire

    print("\nTous les objets obligatoires ont été achetés avec succès ! Voici votre inventaire final :")
    print("Profil du personnage :")
    print("Nom : " + personnage["Nom"])
    print("Prenom : " + personnage["Prenom"])
    print("Argent : " + str(personnage["argent"]))
    print("Inventaire : " + ", ".join(personnage["inventaire"]))
    print("Sortilèges :")
    print("Attributs :")
    for cle in personnage["Attributs"]:
        print("- " + cle + " : " + str(personnage["Attributs"][cle]))

def lancer_chapitre1():
   # introduction()
    personnage= creer_personnage()
    #recevoir_lettre()
    #rencontrer_hagrid(personnage)
    acheter_fournitures(personnage)