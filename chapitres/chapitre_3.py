import json
import random

def apprendre_sorts(joueur, chemin_fichier="data/sorts.json"):
    print("Tu commences tes cours de magie à Poudlard...\n")

    with open(chemin_fichier, "r", encoding="utf-8") as f:
        sorts_disponibles = json.load(f)

    offensifs = [s for s in sorts_disponibles if s["type"].lower() == "offensif"]
    defensifs = [s for s in sorts_disponibles if s["type"].lower() == "défensif"]
    utilitaires = [s for s in sorts_disponibles if s["type"].lower() == "utilitaire"]

    sorts_appris = []
    sort_o = random.choice(offensifs)
    sorts_appris.append(sort_o)
    sort_d = random.choice(defensifs)
    sorts_appris.append(sort_d)
    sorts_util = random.sample(utilitaires, 3)
    sorts_appris.extend(sorts_util)
    joueur["Sortilèges"] = []

    for sort in sorts_appris:
        joueur["Sortilèges"].append(sort)
        print(f"Tu viens d'apprendre le sortilège : {sort['nom']} ({sort['type']})")
        input("Appuie sur Entrée pour continuer...")

    print("\nTu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :")
    for sort in joueur["Sortilèges"]:
        print(f"- {sort['nom']} ({sort['type']}) : {sort['description']}")

def quiz_magie(joueur, chemin_fichier="data/quiz_magie.json"):
    print("\nBienvenue au quiz de magie de Poudlard !")
    print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison.\n")

    with open(chemin_fichier, "r", encoding="utf-8") as f:
        questions = json.load(f)
    questions_tirees = random.sample(questions, 4)

    score_quiz = 0

    for i, q in enumerate(questions_tirees, 1):
        print(f"{i}. {q['question']}")
        reponse = input("> ").strip()
        if reponse.lower() == q["reponse"].lower():
            print("Bonne réponse ! +25 points pour ta maison.\n")
            score_quiz += 25
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {q['reponse']}\n")

    print(f"Score obtenu : {score_quiz} points\n")
    joueur["score"] = joueur.get("score", 0) + score_quiz
def lancer_chapitre_3(joueur, maisons):
    apprendre_sorts(joueur)
    quiz_magie(joueur)
    maison_joueur = joueur["maison"]
    maisons[maison_joueur] += joueur.get("score", 0)

    maison_ennemie = max(maisons, key=maisons.get)
    print(f"La maison actuellement en tête est : {maison_ennemie} avec {maisons[maison_ennemie]} points\n")

    print("=== Informations du joueur ===")
    for cle, valeur in joueur.items():
        if cle != "Sortilèges":
            print(f"{cle.capitalize()} : {valeur}")
    if "Sortilèges" in joueur:
        print("Sortilèges appris :")
        for sort in joueur["Sortilèges"]:
            print(f"- {sort['nom']} ({sort['type']}) : {sort['description']}")
joueur = {"nom": "Harry Potter", "maison": "Gryffondor"}
maisons = {
    "Gryffondor": 0,
    "Serpentard": 0,
    "Serdaigle": 0,
    "Poufsouffle": 0
}
