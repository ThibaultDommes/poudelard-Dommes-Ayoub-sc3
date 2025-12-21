
import json
import random


def _charger_json(chemin):
    fichier = open(chemin, "r", encoding="utf-8")
    data = json.load(fichier)
    fichier.close()
    return data


def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):
    """
    Apprend 5 sorts aléatoires :
    - 1 offensif
    - 1 défensif
    - 3 utilitaires
    Ajoute les sorts dans joueur["Sortilèges"].
    """
    print("Tu commences tes cours de magie à Poudlard...")

    sorts = _charger_json(chemin_fichier)

    # On suppose que sorts est une liste de dictionnaires du style :
    # {"nom": "...", "type": "Offensif"/"Défensif"/"Utilitaire", "description": "..."}
    if "Sortilèges" not in joueur:
        joueur["Sortilèges"] = []

    offensif_ok = 0
    defensif_ok = 0
    utilitaire_ok = 0

    appris = []  # liste des sorts appris (dicos)

    while len(appris) < 5:
        s = random.choice(sorts)

        # éviter doublons (par nom)
        deja = False
        for x in appris:
            if x["nom"] == s["nom"]:
                deja = True
        if deja:
            continue

        t = s.get("type", "")

        if t == "Offensif" and offensif_ok < 1:
            appris.append(s)
            offensif_ok = offensif_ok + 1
        elif t == "Défensif" and defensif_ok < 1:
            appris.append(s)
            defensif_ok = defensif_ok + 1
        elif t == "Utilitaire" and utilitaire_ok < 3:
            appris.append(s)
            utilitaire_ok = utilitaire_ok + 1

        # sinon: on ignore et on retente

    # Ajout au joueur + narration
    for s in appris:
        joueur["Sortilèges"].append(s)
        print("Tu viens d'apprendre le sortilège :", s["nom"], "(" + s["type"] + ")")
        input("Appuie sur Entrée pour continuer...")

    print("Tu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :")
    for s in appris:
        print("-", s["nom"], "(" + s["type"] + ") :", s.get("description", ""))
    print()


def quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json"):
    """
    Pose 4 questions aléatoires sans doublons.
    +25 points par bonne réponse.
    Ajoute le score au score du joueur.
    """
    print("Bienvenue au quiz de magie de Poudlard !")
    print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison.")

    quiz = _charger_json(chemin_fichier)

    # On suppose une liste de dicos :
    # {"question": "...", "reponse": "..."}
    questions_tirees = []
    while len(questions_tirees) < 4:
        q = random.choice(quiz)

        deja = False
        for x in questions_tirees:
            if x["question"] == q["question"]:
                deja = True
        if not deja:
            questions_tirees.append(q)

    score = 0

    i = 1
    for q in questions_tirees:
        print(str(i) + ".", q["question"])
        rep = input("> ").strip()

        bonne = q["reponse"].strip()

        # comparaison simple (insensible à la casse)
        if rep.lower() == bonne.lower():
            print("Bonne réponse ! +25 points pour ta maison.")
            score = score + 25
        else:
            print("Mauvaise réponse. La bonne réponse était :", bonne)
        print()
        i = i + 1

    # Ajout du score au joueur (on crée si absent)
    if "Score" not in joueur:
        joueur["Score"] = 0
    joueur["Score"] = joueur["Score"] + score

    print("Score obtenu :", score, "points")
    print("Score total du joueur :", joueur["Score"], "points")
    print()
