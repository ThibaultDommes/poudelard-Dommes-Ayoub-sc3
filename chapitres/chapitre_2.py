import json

from chapitres.chapitre_1 import creer_personnage
from univers.maison import *
from univers.personnage import *
from utils.input_utils import *


def rencontrer_amis(joueur):
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord...")
    print("Un garçon roux entre dans votre compartiment, l’air amical.")
    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ?")
    c = demander_choix("Que répondez-vous ?", ["Bien sûr, assieds-toi !", "Désolé, je préfère voyager seul."])

    if c == 1:
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable !")
        joueur["Attributs"]["loyaute"] = joueur["Attributs"]["loyaute"] + 1
    else:
        print("Ron hausse les épaules : — Pas de souci... Bonne route alors.")
        joueur["Attributs"]["ambition"] = joueur["Attributs"]["ambition"] + 1

    print()
    print("Une fille entre ensuite, portant déjà une pile de livres.")
    print("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?")
    c = demander_choix("Que répondez-vous ?",["1. Oui, j’adore apprendre de nouvelles choses !","2. Euh... non, je préfère les aventures aux bouquins."] )

    if c == 1:
        print("Hermione sourit : — Oh, merveilleux ! On aura beaucoup à discuter.")
        joueur["Attributs"]["intelligence"] = joueur["Attributs"]["intelligence"] + 1
    else:
        print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un jour !")
        joueur["Attributs"]["courage"] = joueur["Attributs"]["courage"] + 1

    print()
    print("Puis un garçon blond entre avec un air arrogant.")
    print("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    c = demander_choix("Comment réagissez-vous ?", ["1. Je lui serre la main poliment.","2. Je l’ignore complètement.","3. Je lui réponds avec arrogance."])

    if c == 1:
        print("Drago esquisse un sourire satisfait. — Sage décision.")
        joueur["Attributs"]["ambition"] = joueur["Attributs"]["ambition"] + 1
    elif c == 2:
        print("Drago fronce les sourcils, vexé. — Tu le regretteras !")
        joueur["Attributs"]["loyaute"] = joueur["Attributs"]["loyaute"] + 1
    else:
        print("Drago te fixe, surpris et agacé. — On verra bien qui rira le dernier.")
        joueur["Attributs"]["courage"] = joueur["Attributs"]["courage"] + 1

    print()
    print("Le train continue sa route. Le château de Poudlard se profile à l’horizon...")
    print("Tes choix semblent déjà en dire long sur ta personnalité !")
    print("Tes attributs mis à jour :", joueur["Attributs"])
    print()

def mot_de_bienvenue():
    print("Les portes de la Grande Salle s’ouvrent dans un silence solennel...")
    print("Le professeur Dumbledore s’avance, son regard pétillant derrière ses lunettes.")
    print("— Bienvenue à Poudlard !")
    print("— Que cette année vous apporte apprentissage, amitié, et courage.")
    print("— N’oubliez jamais : vos choix révèlent qui vous êtes vraiment.")
    input("Appuie sur Entrée pour continuer...")


def ceremonie_repartition(joueur):
    questions = [
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te décrit le mieux ?",
            ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, tu...",
            ["Fonces sans hésiter", "Cherches la meilleure stratégie", "Comptes sur tes amis", "Analyses le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]

    print("La cérémonie de répartition commence dans la Grande Salle...")
    print("Le Choixpeau magique t’observe longuement avant de poser ses questions :")
    maison = repartition_maison(joueur, questions)
    joueur["Maison"] = maison

    print("Le Choixpeau s’exclame :", maison, "!!!")
    print("Tu rejoins les élèves de", maison, "sous les acclamations !")
    print()


def installation_salle_commune(joueur):
    print("Vous suivez les préfets à travers les couloirs du château...")
    maison = joueur.get("Maison", "")

    with open('data/maisons.json', "r", encoding="utf-8") as fichier :
        data = json.load(fichier)

    if maison == "" or maison not in data:
        print("Erreur : maison inconnue. Impossible d’installer le joueur.")
        return

    infos = data[maison]
    description = infos.get("description", "")
    accueil = infos.get("message_accueil", "")
    couleurs = infos.get("couleurs", [])

    print(description)
    print(accueil)

    if type(couleurs) == list:
        print("Les couleurs de votre maison :", ", ".join(couleurs))
    else:
        print("Les couleurs de votre maison :", couleurs)

    print()

def lancer_chapitre_2(personnage):
    rencontrer_amis(personnage)
    mot_de_bienvenue()
    ceremonie_repartition(personnage)
    installation_salle_commune(personnage)
    afficher_personnage(personnage)

    print(" Fin du chapitre 2 : Le voyage vers Poudlard est terminé.")
    print(" Le chapitre 3 va commencer : place aux cours de magie !")
    input("Appuie sur Entrée pour continuer...")
