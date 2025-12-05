from utils.input_utils import *

if __name__ == '__main__':
    message = input("Entrez le nom de votre personnage : ")
    demander_texte(message)
    print(message)
    demander_choix(message,1,10)