# tictactoe

print("Bienvenue au jeu du tic tac toe!")

# initialisation de la grille en forme de liste de listes

grille = [['', '', ''],
          ['', '', ''],
          ['', '', '']]

alph = ["a","b","c"] # on initialise une liste contenant les lettres réprésentant chaque ligne de la grille 

# initialisation de la variable du joueur dont le premier sera le symbole X
joueur_en_cours = 'X'

# fonction permettant d'afficher la grille
def affiche_grille(grille):

    # boucle qui va print 0, 1 et 2 representant chaque colonne
    for j in range(3):
        print(" ", j, end="")
    print()
    # boucles qui print les lettres avec les lignes qu'elles representent
    for l, ligne in zip(alph, grille):
        print(l, end="")
        for symbole in ligne:
            print("|_{}_".format(symbole), end="")
        print()

def placer(joueur_en_cours,ligne,colonne,grille): #place les pions en vérifiant si la case choisie n'est pas déjà prise
    if grille[alph.index(ligne)][colonne] == '':
        grille[alph.index(ligne)][colonne] = joueur_en_cours
        return True
    else:
        print("Déjà pris. Réesseyez")
        return False
    
# fonction qui vérifie si un joueur a gagné en parcourant la grille
def victoire(grille,joueur_en_cours):
    # verification de victoire ligne
    for ligne in grille:
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] == joueur_en_cours :
            return True
    # verification victoire colonne
    for colonne in range(3):
        if grille[0][colonne] == grille[1][colonne] == grille[2][colonne] and grille[0][colonne] == joueur_en_cours:
            return True
    # verification victoire diagonale
    if (grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] == joueur_en_cours) or (grille[0][2] == grille[1][1] == grille[2][0] and grille[0][2] == joueur_en_cours):
        return True
    
    return False
    
# boucle du jeu 
while True:
    affiche_grille(grille)
    print("C'est au tour du joueur", joueur_en_cours)

    # Demande de ligne et de colonne
    try:
        ligne = input("Entrez la lettre correspondant à la ligne (a, b, c) : ")
        colonne = int(input("Entrez le numéro de colonne (0, 1, 2) : "))
    except ValueError:
        print("Veuillez entrer des nombres valides.")
        continue

 # verifie si le joueur a saisie une combinaison valide et verifie le placement+victoire en appelant les fonctions
    if ligne in alph and 0 <= colonne < 3:
        if placer(joueur_en_cours,ligne,colonne,grille):
            if victoire(grille,joueur_en_cours):
                affiche_grille(grille)
                print("Le joueur",joueur_en_cours,"a gagné !")
                break
            joueur_en_cours = 'X' if joueur_en_cours == 'O' else 'O'
        else:
            continue
    else:
        print("Veuillez saisir des valeurs valides.")
        continue