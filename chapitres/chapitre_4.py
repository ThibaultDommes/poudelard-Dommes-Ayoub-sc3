import json
import random

with open("data/equipes_quidditch.json", "r", encoding="utf-8") as f:
    equipes = json.load(f)


def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    equipe = {
        "nom": maison,
        "score": 0,
        "a_marque": 0,
        "a_stoppe": 0,
        "attrape_vifdor": False,
        "joueurs": list(equipe_data["joueurs"])
    }

    if est_joueur and joueur is not None:
        nouvelle_liste = []

        nouvelle_liste.append(f"{joueur['Nom']} (Attrapeur)")

        for j in equipe_data["joueurs"]:
            if joueur["Nom"] not in j:
                nouvelle_liste.append(j)

        equipe["joueurs"] = nouvelle_liste

    return equipe

def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = random.randint(1, 10)

    if proba_but >= 6:
        if joueur_est_joueur:
            buteur = equipe_attaque["joueurs"][0]
        else:
            buteur = random.choice(equipe_attaque["joueurs"])

        equipe_attaque["score"] += 10
        equipe_attaque["a_marque"] += 1

        print(f"{buteur} marque un but pour {equipe_attaque['nom']} ! (+10 points)")
    else:
        equipe_defense["a_stoppe"] += 1
        print(f"{equipe_defense['nom']} bloque l’attaque !")

equipe_gryffondor = creer_equipe("Gryffondor", equipes["Gryffondor"], est_joueur=True)
equipe_serpentard = creer_equipe("Serpentard", equipes["Serpentard"])

print(tentative_marque(equipe_gryffondor,equipe_serpentard, joueur_est_joueur=True))

def apparition_vifdor():
    return random.randint(1, 6) == 6

def attraper_vifdor(e1, e2):
    gagnante = random.choice([e1, e2])
    gagnante["score"] += 150
    gagnante["attrape_vifdor"] = True

    print(f"Le Vif d’Or a été attrapé par {gagnante['nom']} ! (+150 points)")
    return gagnante

def afficher_score(e1, e2):
    print("Score actuel :")
    print(f"→ {e1['nom']} : {e1['score']} points")
    print(f"→ {e2['nom']} : {e2['score']} points")

def afficher_equipe(maison, equipe):
    print(f"\nÉquipe de {maison} :")
    for joueur in equipe["joueurs"]:
        print(f"- {joueur}")

def match_quidditch(joueur, maisons):
    maison_joueur = joueur["maison"]

    maisons_adverses = [m for m in maisons if m != maison_joueur]
    maison_adverse = random.choice(maisons_adverses)

    equipe_joueur = creer_equipe(maison_joueur, equipes[maison_joueur], est_joueur=True, joueur=joueur)
    equipe_adverse = creer_equipe(maison_adverse, equipes[maison_adverse])

    print(f"\nMatch de Quidditch : {maison_joueur} vs {maison_adverse} !")
    afficher_equipe(maison_joueur, equipe_joueur)
    afficher_equipe(maison_adverse, equipe_adverse)

    print(f"\nTu joues pour {maison_joueur} en tant qu’Attrapeur\n")

    for tour in range(1, 21):
        print(f"\n━━━ Tour {tour} ━━━")
        tentative_marque(equipe_joueur, equipe_adverse, joueur_est_joueur=True)
        tentative_marque(equipe_adverse, equipe_joueur, joueur_est_joueur=False)

        afficher_score(equipe_joueur, equipe_adverse)

        if apparition_vifdor():
            gagnant_vif = attraper_vifdor(equipe_joueur, equipe_adverse)
            print("\nFin du match anticipée à cause du Vif d’Or !")
            afficher_score(equipe_joueur, equipe_adverse)
            break

        input("Appuyez sur Entrée pour passer au tour suivant...")

    if not equipe_joueur["attrape_vifdor"] and not equipe_adverse["attrape_vifdor"]:
        print("\n━━━ Fin du match ━━━")
        afficher_score(equipe_joueur, equipe_adverse)

    if equipe_joueur["score"] > equipe_adverse["score"]:
        gagnant = equipe_joueur
    elif equipe_adverse["score"] > equipe_joueur["score"]:
        gagnant = equipe_adverse
    else:
        gagnant = None

    print("\n=== Résultat final ===")
    if gagnant:
        print(f"La maison gagnante est {gagnant['nom']} avec {gagnant['score']} points !")
    else:
        print("Match nul ! Les deux équipes ont le même score.")


def lancer_chapitre4_quidditch(joueur, maisons):
    print("\n=== Chapitre 4 : Épreuve de Quidditch ===\n")
    match_quidditch(joueur, maisons)

    print("\nFin du Chapitre 4 — Quelle performance incroyable sur le terrain !\n")

    maison_gagnante = max(maisons, key=maisons.get)
    print(f"La maison qui remporte la Coupe des Quatre Maisons est {maison_gagnante} !\n")
    print("=== Informations du personnage ===")
    for cle, valeur in joueur.items():
        print(f"{cle.capitalize()} : {valeur}")
