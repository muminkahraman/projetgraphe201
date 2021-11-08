import os

def choixDuFichier (cheminDuRepertoire) :
    list = os.listdir(cheminDuRepertoire)
    incr = 0
    print('voici la liste des fichier dans le répertoire /n que vous avec donné : ')
    for i in list :
        incr += 1
        print(incr, "-", i)
    choix = int(input('entrez le numéro du fichiez que vous voulez choisir : ')) - 1
    return choix;

def rechercheDeGrapheDansFichier(repertoire, choixFichier):
    list = list = os.listdir(repertoire)
    nomFichier = list[choixFichier];
    fichier = open(repertoire + '/' + nomFichier, 'r')
    lignes = fichier.readlines()
    print(lignes)
    for i in range (len(lignes)):
        lignes[i] = lignes[i].split(";")
    for i in range(len(lignes)-1):
        lignes[i][-1] = lignes[i][-1].replace('\n', '')
    return lignes

def afficherMatrice(matrice):
    for row in matrice:
        for val in row:
            print'{:4}'.format(val),
        print


#--------------PROGRAMME PRINCIPAL----------------------------------

print("#####################################################################")
print("#                          Projet Graphe                            #")
print("#####################################################################\n")
repertoire = input('entrez le chemin du répertoire contenant les fichiers graph : ')
repertoireTest = './txtPourTest'
#choixFichier = choixDuFichier(repertoire)
choixFichier = choixDuFichier(repertoireTest)
#rechercheDeGrapheDansFichier(repertoire, choixFichier)
matrice = rechercheDeGrapheDansFichier(repertoireTest, choixFichier)
afficherMatrice(matrice)