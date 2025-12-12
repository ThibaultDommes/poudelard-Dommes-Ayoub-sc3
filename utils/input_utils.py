import json

def demander_texte(message):
    while message == "":
        message = input("Entrez le nom de votre personnage : ")
    else :
        return message
#texte = demander_texte(input("Entrez le nom de votre personnage : "))


def demander_nombre(message,min_val,max_val):
    texte = message +" (" +str(min_val)+","+str(max_val)+")"": "
    nb = int(input(texte))
    while nb < min_val or nb > max_val :
        fin = "Veuillez entrer un nombre entre"+ str(min_val) +"et" + str(max_val),"  : "
        print(fin)
        nb = int(input(texte))
    print("Votre " + message + " est de : "+ str(nb))
    return nb
#a = demander_nombre("Niveau de courage",0,10)


def demander_choix(message,options):
    print(message)
    for i in range(len(options)):
        print(i+1,options[i])
    choix = int(input("Quel est votre choix : "))
    while isinstance(choix,int) or choix not in options[]:
        choix = int(input("Quel est votre choix : "))
    return choix
b = demander_choix("Voulez-vous continuer ?", ["Oui", "Non"])


def load_fichier(chemin_fichier):
    with open('data.json', 'r', encoding='utf-8') as f:
        donnees = json.load(f)
    return donnees