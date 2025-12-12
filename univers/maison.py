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