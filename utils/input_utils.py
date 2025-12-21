import json

def demander_texte(message):
    texte = input(message)
    valide = False

    while valide == False:
        if texte == "":
            print("Le texte ne peut pas être vide.")
            texte = input(message)
        else:
            contient_chiffre = False
            for caractere in texte:
                if caractere >= '0' and caractere <= '9':
                    contient_chiffre = True
                    break

            if contient_chiffre:
                print("Le texte ne doit pas contenir de chiffres.")
                texte = input(message)
            else:
                # La saisie est valide
                valide = True

    return texte

#nom = demander_texte("Entrez le nom de votre personnage : ")
#print("Nom choisi :", nom)

"""def demander_nombre(message,min_val,max_val):
    texte = message +" (" +str(min_val)+","+str(max_val)+")"": "
    nb = int(input(texte))
    while nb < min_val or nb > max_val :
        fin = "Veuillez entrer un nombre entre"+ str(min_val) +"et" + str(max_val),"  : "
        print(fin)
        nb = int(input(texte))
    print("Votre " + message + " est de : "+ str(nb))
    return nb
"""
def demander_nombre(message, min_val, max_val):
    texte = message + " (" + str(min_val) + "-" + str(max_val) + ") : "
    saisie = input(texte)
    valide = False

    while valide == False:
        # Vérifier que la saisie n'est pas vide
        if saisie == "":
            print("Vous devez entrer un nombre.")
            saisie = input(texte)
        else:
            est_nombre = True
            for caractere in saisie:
                if caractere < '0' or caractere > '9':
                    est_nombre = False
                    break

            if est_nombre == False:
                print("Vous devez entrer un nombre valide.")
                saisie = input(texte)
            else:
                nb = int(saisie)
                if nb < min_val or nb > max_val:
                    print("Veuillez entrer un nombre entre " + str(min_val) + " et " + str(max_val) + ".")
                    saisie = input(texte)
                else:
                    # La saisie est valide
                    valide = True

    print("Votre " + message + " est de : " + str(nb))
    return nb

#a = demander_nombre("Niveau de courage",0,10)

def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print(i + 1, options[i])
    choix = input("Quel est votre choix : ")
    choix_valide = False
    while choix_valide == False:
        est_nombre = True
        for caractere in choix:
            if caractere < '0' or caractere > '9':
                est_nombre = False

        if est_nombre == True:
            choix_int = int(choix)
            if choix_int >= 1 and choix_int <= len(options):
                choix_valide = True
            else:
                print("Le choix n'est pas dans la liste.")
        else:
            print("Le choix doit être un nombre.")

        if choix_valide == False:
            choix = input("Quel est votre choix : ")

    return choix_int

#b = demander_choix("Voulez-vous continuer ?", ["Oui", "Non"])


def load_fichier(chemin_fichier):
    with open('data.json', 'r', encoding='utf-8') as f:
        donnees = json.load(f)
    return donnees