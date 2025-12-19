from utils.input_utils import demander_choix

def initialiser_maisons(liste_noms):
    maisons = {}
    for nom in liste_noms:
        maisons[nom] = 0
    return maisons
def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] = maisons[nom_maison] + points
        print("La maison", nom_maison, "gagne", points, "points.")
    else:
        print("Maison inconnue :", nom_maison)


def afficher_maison_gagnante(maisons):
    max_points = None
    for nom in maisons:
        pts = maisons[nom]
        if max_points is None or pts > max_points:
            max_points = pts

    gagnantes = []
    for nom in maisons:
        if maisons[nom] == max_points:
            gagnantes.append(nom)

    print("===== Résultat final des maisons =====")
    for nom in maisons:
        print("-", nom, ":", maisons[nom], "points")

    if len(gagnantes) == 1:
        print("Maison gagnante :", gagnantes[0])
    else:
        print("Maisons ex æquo :")
        for nom in gagnantes:
            print(" -", nom)

def repartition_maison(joueur, questions):

    scores = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    attributs = joueur["Attributs"]
    scores["Gryffondor"] = scores["Gryffondor"] + attributs["courage"]
    scores["Serpentard"] = scores["Serpentard"] + attributs["ambition"]
    scores["Poufsouffle"] = scores["Poufsouffle"] + attributs["loyaute"]
    scores["Serdaigle"] = scores["Serdaigle"] + attributs["intelligence"]

    for q in questions:
        texte_q = q["texte"]
        options = q["options"]
        maisons_associees = q["maisons"]

        reponse = demander_choix(texte_q, options)

        index = 0
        while index < len(options) and options[index] != reponse:
            index = index + 1

        if index < len(maisons_associees):
            maison = maisons_associees[index]
            scores[maison] = scores[maison] + 3

    maison_finale = None
    max_points = None
    for nom in scores:
        pts = scores[nom]
        if max_points is None or pts > max_points:
            max_points = pts
            maison_finale = nom

    print("Scores de répartition :")
    for nom in scores:
        print("-", nom, ":", scores[nom], "points")

    return maison_finale