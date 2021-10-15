import os

dir = os.path.split(__file__)[0]
Extentions = ['.txt','.TXT']
inf=float('inf')

def readGraph(filedir):
    file=open(filedir)
    size = int(file.readline().split()[0])
    nbArc = int(file.readline().split()[0])
    mat = [[float('inf')]*int(size) for i in range(int(size))]
    for i in range(int(size)):mat[i][i]='0'
    for i in range(nbArc):
        line = file.readline().split()
        n = int(line[0])
        m = int(line[1])
        mat[n][m] = float(line[2])
    return nbArc, size, mat

def printGraph(graph):
    print("Sommet ",end='',flush=True)
    for i in range(graph[1]):
        print("   "+str(i)+"    ",end='',flush=True)
    print("")
    for i in range(graph[1]):
        print(" "+str(i)+" :   ",end='',flush=True)
        for j in range(graph[1]):
            print("[  "+ str(graph[2][i][j]) +" "*(5-len(str(graph[2][i][j])))+"]", end="", flush=True)
        print()

#Fonction qui affiche le menu et la liste des graphes
def choixGraph(graphList):
    print("Choisissez le graph a traiter : ")
    for i in range(len(graphList)):
        print(str(i+1)+") Graph ["+graphList[i][3][:-4]+"] =<S,A> / Cardinalité(S) = "+str(graphList[i][1])+" / Cardinalité(A) = "+str(graphList[i][0])+".")
    print("\t [0] Pour quitter.")
    val = int(input("\t   Votre choix : "))
    if(val < 0 or val > len(graphList)):print("\n\n[Veuillez effectuer un choix valide...]\n\n")
    return val
graphs = []

#Utilisation de readGraph pour charger tout les graphes en memoire d'apres leur fichier
for file in os.listdir(dir):
    if(file[-4:] in Extentions):
        nbArc, size, mat = readGraph(dir+'/'+file)
        graphs.append((nbArc, size, mat, file))
        
val = len(graphs)

#implémentation de l'algorithme
def floydWarshall(Graph):
    size = int(Graph[1])
    temp = Graph[2]
    
    D = [[float('inf')]*size for i in range(size)]
    P = [[(float('nan'),'pred')]*size for i in range(size)]
    cycleABS=False
    for i1 in range(size):
        for j1 in range(size):
            if(float(temp[i1][j1])<inf):
                P[i1][j1] = (float(temp[i1][j1]),'pred')
                D[i1][j1] = float(temp[i1][j1])
    return P,cycleABS,D

#Boucle pour continuer a traiter n graphes tantque l'utilisateur ne choisis pas de quitter
while (val > 0 and val <= len(graphs)): 
    val = choixGraph(graphs)
    if(val == 0):
        print("\tFin du programme")
        break
    if(val > 0 and val <= len(graphs)):
        G=graphs[val-1]
        printGraph(G)
        input("  Faite rentré une valeur pour commencer le traitement : ")
        P,bol,D=floydWarshall(graphs[val-1])
        printGraph((G[0],G[1],P,G[3]))
    else: val = len(graphs)
