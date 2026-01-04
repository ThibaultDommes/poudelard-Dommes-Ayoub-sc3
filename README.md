# poudelard-Dommes-Ayoub-sc3
Titre du projet: Aventure Poudlard

Description brève : 

C'est l'histoire d'un personnage qui s'aventure dans le monde de Poudlard et comme 
dans les films il a donc une maison,participe à des combats contre des arraignées et encore participe à une épreuve de Quidditch
Le jeu entier se repose sur des choix arbitraires réalisé par l'utilisateur.

Contributeurs :
Sam Ayoub
Thibault Dommes

Installations :
https://github.com/ThibaultDommes/poudelard-Dommes-Ayoub-sc3.git

Fonctionnalités principales : 

Création et personnalisation du personnage
Progression à travers les différents chapitres 
Gestion des discussions tout au long de l'aventure
Gestion des maisons et scores associés.

Chronologie du projet :
28/11/2025 : Création du projet 
05/12/2025 : Réalisation des fonctions dans personnage et début de input_utils
12/12/2025 : Fin input_utils et démarrage de chapitre1 et réalisation de maison entièrement
19/12/2025 : Correction complète et implémentation de fonctionnalités facultatives dans plusieurs fonctions
21/12/2025 : Fin du chapitre 1, Chapitre 2 entier et début de Chapitre 3
04/01/2026 : Fin chapitre 3, Chapitre 4 entier, Chapitre 5 entier et menu

Répartiton des tâches : 
Sam Ayoub : Personnage, Maison, Chapitre 2,Chapitre 5 readme
Thibault Dommes : input_utils, Chapitre 1,Chapitre 3,Chapitre 4,menu, readme

Gestion des Entrees et Erreurs
Pour la fonction demander_choix dans input_utils elle gère tout les types d'erreurs : Valeur vide, Caractère et choix hors liste
Pour demander_texte la fonction gère également si le texte est soit un int soit vide et redemande tant que l'utilisateur renvoit une chaine de caractère
En revanche pour demander_choix et demander_nombre on ne gère pas le renvoit vide

Le code utilise surtout des nombres pour compter les points et des mots pour les noms des maisons. 
Les points sont ajoutés petit à petit et le programme compare les valeurs pour trouver le plus grand score. 
Les listes sont parcourues en faisant attention à ne pas dépasser leur taille.
Les erreurs sont limitées grâce à des vérifications simples, comme tester si une maison existe avant d’ajouter des points, 
et grâce à la fonction demander_choix qui oblige l’utilisateur à choisir une réponse correcte.
égalités mal gérées et données mal écrites possibles.

Bugs ou limites connus : si deux maisons ont le même score, une seule est choisie ; si les données ne sont pas bien écrites, 
Le programme peut mal fonctionner,certaines situations ne sont pas signalées par un message d’erreur.
En revanche pour demander_choix et demander_nombre on ne gère pas le renvoit vide
Si les données du joueur sont mal renseignées on gère mal
Le code ajoute et compare des points pour choisir une maison.
demander_choix limite les erreurs de réponse.
Limites : égalités mal gérées et données mal écrites possibles.

Capture d'écrans ; 
https://prnt.sc/2YapuVZsxE81
https://prnt.sc/w7VdYxzWVgQh
https://prnt.sc/3riMHF4ftaH1
https://prnt.sc/_6t48xa8_Hgu
https://prnt.sc/YscxcVx2N5Ky
https://prnt.sc/H1Afl3QBJ6RT
https://prnt.sc/4Y88qGGSynHm
https://prnt.sc/PMvxeFtzKSpo
https://prnt.sc/yrRv5OIiXZWq
https://prnt.sc/WFLanN8wd9_B
https://prnt.sc/iU_Eh0IYTSzP
https://prnt.sc/d_XH8b_xBpzX
https://prnt.sc/EdwMZZ9X0q-F
https://prnt.sc/5073WZEd-Dn4
https://prnt.sc/SGcG9kVhPHlz
https://prnt.sc/6rGQVSk8WwzB
