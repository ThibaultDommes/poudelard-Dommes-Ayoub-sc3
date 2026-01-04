from chapitres.chapitre_1 import lancer_chapitre1
from chapitres.chapitre_2 import lancer_chapitre_2
from chapitres.chapitre_3 import lancer_chapitre_3
from chapitres.chapitre_4 import lancer_chapitre4_quidditch
from chapitres.chapitre_5_extension import chapitre_5
from utils.input_utils import demander_choix

def afficher_menu_principal():
    print("\n=== Menu Principal ===")


def lancer_choix_menu():
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Serdaigle": 0,
        "Poufsouffle": 0
    }

    while True:
        afficher_menu_principal()
        choix = demander_choix("Choisis une option :", ["Lancer l'aventure complète", "Quitter le jeu"])

        if choix == 1:
            personnage = lancer_chapitre1()
            lancer_chapitre_2(personnage)
            lancer_chapitre_3(personnage, maisons)
            lancer_chapitre4_quidditch(personnage, maisons)
            personnage, maisons = chapitre_5(personnage, maisons)

            print("\n=== Résultat final des maisons ===")
            for maison, score in maisons.items():
                print(f"{maison} : {score} points")
            print("\nMerci d'avoir joué ! L'aventure est terminée.\n")

        elif choix == 2:
            print("Merci d'avoir joué. À bientôt !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    lancer_choix_menu()
