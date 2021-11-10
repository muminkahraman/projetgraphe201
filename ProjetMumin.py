import os


def choixDuFichier (cheminDuRepertoire) :
    list = os.listdir(cheminDuRepertoire)
    incr = 0
    print('\nvoici la liste des fichier dans le répertoire que vous avec donné : ')
    for i in list :
        incr += 1
        print(incr, "-", i)
    choix = int(input('entrez le numéro du fichiez que vous voulez choisir : ')) - 1
    return choix;


def rechercheDeGrapheDansFichier(repertoire, choixFichier, savedMatrixes):
    list = list = os.listdir(repertoire)
    nomFichier = list[choixFichier];
    fichier = open(repertoire + '/' + nomFichier, 'r')
    lignes = fichier.readlines()
    for i in range (len(lignes)):
        lignes[i] = lignes[i].split(";")
    for i in range(len(lignes)-1):
        lignes[i][-1] = lignes[i][-1].replace('\n', '')
    saveMatriceDansMemoire(lignes, savedMatrixes)
    return lignes


def afficherMatrice(matrice):
    maxlen = 0
    for ligne in matrice:
        if (len(max(ligne, key=len)) > maxlen):
            maxlen = len(max(ligne, key=len))+1
        else:
            pass
    for ligne in matrice:
        ligneStr =''
        for elem in ligne:
            ajout = elem + ' '
            while (len(ajout) < maxlen):
                ajout += ' '
            ligneStr += ajout
        print(ligneStr[:-1])


def saveMatriceDansMemoire(matrice, savedMatrixes):
    print("\n")
    afficherMatrice(matrice)
    print("\nvoulez vous enregistrer cette matrice dans la mémroire du programme ?\n"
          "1 - Oui\n"
          "2 - Non")
    choixSave = input("entrez votre choix : ")
    if(choixSave == "1"):
        savedMatrixes.append(matrice)
        print("Matrice enregistrée dans la mémoire du programme avec succes")
    else:
        print("Matrice non enregistrée")


def printSavedMatrixes(savedMatrixes):
    print("\nles matrices enregistrées sont :")
    for matrixe in savedMatrixes:
        savedMatrixes.index(matrixe)

#--------------PROGRAMME PRINCIPAL----------------------------------

def main():
    print("#####################################################################")
    print("#                          Projet Graphe                            #")
    print("#####################################################################\n")
    savedMatrixes = []
    while(1):
        print("\nMenu : \n"
              "1 - charger une matrice depuis fichier txt.\n"
              "2 - chosir une matrice déja enregistrée.")
        choixMenu = input("entrez le numéro de l'action choisie : ")
        if (int(choixMenu) == 1):
            repertoire = input('\nentrez le chemin du répertoire contenant les fichiers graph : ')
            repertoireTest = './txtPourTest'
            # choixFichier = choixDuFichier(repertoire)
            choixFichier = choixDuFichier(repertoireTest)
            # rechercheDeGrapheDansFichier(repertoire, choixFichier)
            matrice = rechercheDeGrapheDansFichier(repertoireTest, choixFichier, savedMatrixes)
            input("tapez une touche pour continuer.")
        elif(int(choixMenu) == 2):
            printSavedMatrixes(savedMatrixes)
        else:
            print("\nVotre entrée ne correspont à aucun élément du Menu.")


if __name__ == "__main__":
    main()
else :
    pass
