from utils.input_utils import *

if __name__ == '__main__':
    message = input("Entrez le nom de votre personnage : ")
    demander_texte(message)
    demander_nombre("Niveau de courage",1,10)
    demander_choix("Voulez-vous continuer ?", ["Oui", "Non"])
