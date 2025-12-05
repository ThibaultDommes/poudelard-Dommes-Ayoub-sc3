def initialiser_personnage(nom, prenom, attributs):
    joueur = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortilèges": [],
        "Attributs": attributs
    }
    return joueur


def afficher_personnage(joueur):
    print("Profil du personnage :")
    for cle in joueur:

        valeur = joueur[cle]
        if type(valeur) == dict:
            print(cle, ":")
            for sous_cle in valeur:
                print(" -", sous_cle, ":", valeur[sous_cle])


