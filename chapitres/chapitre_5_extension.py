import random

def chapitre_5(joueur, maisons):
    print("\n--- Chapitre 5 : La Forêt interdite ---")
    print("Des araignées géantes t’attaquent !")

    pv_joueur = 20
    pv_araignees = 15
    maison = joueur["maison"]

    while pv_joueur > 0 and pv_araignees > 0:
        print(f"\nTes PV : {pv_joueur} | Araignées : {pv_araignees}")
        choix = input("1 - Attaquer  |  2 - Se soigner : ").strip()

        if choix == "1":
            degats = random.randint(3, 6)
            pv_araignees = max(0, pv_araignees - degats)
            print(f"Tu lances un sort ! Les araignées perdent {degats} PV.")
        elif choix == "2":
            soin = random.randint(2, 4)
            pv_joueur += soin
            print(f"Tu te soignes de {soin} PV.")
        else:
            print("Choix invalide ! Les araignées en profitent...")
            degats_araignees = 0

        degats_araignees = random.randint(3, 5)
        pv_joueur = max(0, pv_joueur - degats_araignees)
        print(f"Les araignées t’attaquent : -{degats_araignees} PV")

    if pv_joueur > 0:
        print("\nVictoire ! Tu échappes aux araignées.")
        maisons[maison] += 50
        print(f"+50 points pour {maison} !")
    else:
        print("\nDéfaite… Les araignées ont gagné.")

    print("\nFin du Chapitre 5.\n")
    return joueur, maisons

if __name__ == "__main__":
    joueur = {"nom": "Harry Potter", "maison": "Gryffondor"}
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Serdaigle": 0,
        "Poufsouffle": 0
    }

    joueur, maisons = chapitre_5(joueur, maisons)
    print("Points actuels des maisons :", maisons)
