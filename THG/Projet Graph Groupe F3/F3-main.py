import os

#Récupère le répertoire de tous les graphiques situés dans le répertoire des programmes.
dir = os.path.split(__file__)[0]

Extentions = ['.txt','.TXT']
inf=float('inf')

#Lit un graphique dans le répertoire en utilisant son nom de fichier
def readGraph(filedir):
    file=open(filedir)
    size = int(file.readline().split()[0])
    nbArc = int(file.readline().split()[0])
    #Tout les sommets sont initialisés a 'inf'
    mat = [[float('inf')]*int(size) for i in range(int(size))]
    for i in range(int(size)):mat[i][i]='0'
    for i in range(nbArc):
        line = file.readline().split()
        n = int(line[0])
        m = int(line[1])
        mat[n][m] = float(line[2])
    return nbArc, size, mat

#Affichage normalisé du graph
def printGraph(graph):
    print("Sommet ",end='',flush=True)
    for i in range(graph[1]):
        print("   "+str(i+1)+"     ",end='',flush=True)
    print("")
    for i in range(graph[1]):
        print(" "+str(i+1)+" :   ",end='',flush=True)
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

#fonction d'affichage qui permet de recuperer le sommet que nous allons utiliser 
def choixSommet(graph, etatSommet):
    print("\n  Choisisser " + etatSommet + " entre 1 et "+str(graph[1])+" [ou faite rentrer (0) pour choisir un autre graph] : ", end='')
    val=int(input())
    while (val<0 or val>graph[1]):
        val=int(input("\t veillez faire un choix valide : "))
    return val
        
#fonction d'affichage qui permet de recuperer l'indice de l'action a fair apres avoir choisis un sommet
def actionSommet():
    action = int(input("Que voulez vous fair : \n\t"
                           +"(1) trouver le chemain le plus court vers un sommet precis\n\t"
                           +"(2) trouver le chemain le plus court vers tout les sommets\n\t"
                           +"(0) Quitter\n\t"
                           +"      Votre choix : "))
    while (action<0 or action >2):
        action = int(input("[Veuillez fair un choix valide]\nQue voulez vous fair : \n\t"
                           +"(1) trouver le chemain le plus court vers un sommet precis\n\t"
                           +"(2) trouver le chemain le plus court vers tout les sommets\n\t"
                           +"(0) Quitter\n\t"
                           +"      Votre choix : "))
    return action

#fonction d'affichage des resultat selon l'action choisie            
def traitementSommet(graph, sd, a, nxt):
    if(a == 1):
        sommetArrivé = choixSommet(graph, "le sommet d'arrive") - 1
        if (get_path(nxt,sd,sommetArrivé)==None):
            print("Aucun chemain disponible entre le sommet " + str(sd+1) + " et le sommet " + str(sommetArrivé+1))
        else :
            print("le chemain le plus court entre le sommet " + str(sd+1) + " et le sommet " + str(sommetArrivé+1) + " est : ", end='')
            print(get_path(nxt,sd,sommetArrivé))
    else : 
        if (a == 2):
            for i in range(graph[1]):
                if (get_path(nxt,sd,i)==None):
                    print("Aucun chemain disponible entre le sommet " + str(sd+1) + " et le sommet " + str(i+1))
                else :
                    print("le chemain le plus court entre le sommet " + str(sd+1) + " et le sommet " + str(i+1) + " est : ", end="")
                    print(get_path(nxt,sd,i))
        else : print("\t\tChoisissez un nouveau sommet : ")
        
graphs = []
    
#Implémentation de l'algorithme de Floyd Warshall
def floydWarshall(graph):
    size = graph[1]
    mat = graph[2]
    negative = False
    dist = [[float("inf")]*size for i in range(size)]
    nxt = [[None] * size for i in range(size)]
    #Initialisation des Matrices
    for i in range(size):
        for j in range(size):
            if mat[i][j] != inf:
                u, v, w = i, j, mat[i][j]
                dist[u][v] = w
                nxt[u][v] = v
    for v in range(size):
        dist[v][v] = 0
        nxt[v][v] = v
    #l'algorithme commence a mettre a jour la matrice des distances en prenant k comme pivot a chaque iteration et remplis la matrice des successeurs
    if (negative == False):
        for k in range(size):
            for i in range(size):
                for j in range(size):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        nxt[i][j] = nxt[i][k]
                        
                        if(i==j and dist[i][j]<0):
                            print("\n\tMatrice des distances les plus court entre chaque sommet iteration "+str(k)+" : ")
                            printGraph((0,len(dist),dist))
                            print("\n\tMatrice des successeurs iteration "+str(k)+" : ")
                            printGraph((0,len(nxt),nxt))
                            negative =True
                            return dist, nxt, negative
            print("\n\tMatrice des distances les plus court entre chaque sommet iteration "+str(k)+" : ")
            printGraph((0,len(dist),dist))
            print("\n\tMatrice des successeurs iteration "+str(k)+" : ")
            printGraph((0,len(nxt),nxt))
    return dist, nxt, negative

#Utilise la matrice des successeurs pour construire le chemain le plus court entre 2 sommets
def get_path(nxt, u, v):
    if nxt[u][v] is None:
        return None
    path = [u+1]
    cout = 0
    while u != v:
        u = nxt[u][v]
        cout += dist[u][v]
        path.append(u+1)
    return path

#Utilisation de readGraph pour charger tout les graphes en memoire d'apres leur fichier
for file in os.listdir(dir):
    if(file[-4:] in Extentions):
        nbArc, size, mat = readGraph(dir+'/'+file)
        graphs.append((nbArc, size, mat, file))
        
val = len(graphs)

#Boucle pour continuer a traiter n graphes tantque l'utilisateur ne choisis pas de quitter
while (val > 0 and val <= len(graphs)): 
    val = choixGraph(graphs)
    if(val == 0):
        print("\tFin du programme")
        break
    if(val > 0 and val <= len(graphs)):
        G=graphs[val-1]
        printGraph(G)
        input("\n  Cliquer sur Enter pour commencer le traitement : ")
        dist, nxt, negative = floydWarshall(G)
        if(negative):input("\n  Un cycle absorbant a été détecté dans le graph, arret de l'algorithme\n\t"
                           +"   Cliquer sur enter pour choisir un autre graph : ")
        else:
            sommetDepart=choixSommet(G,"le sommet de depart")-1
            if(sommetDepart != -1):
                while (sommetDepart> -1 and sommetDepart<G[1]):
                    action = actionSommet()
                    while action != 0:
                        traitementSommet(G, sommetDepart, action, nxt)
                        input("\nCliquer sur Enter pour revenir aux actions possibles sur le sommet " + str(sommetDepart + 1) + " : ")
                        action = actionSommet()
                    sommetDepart=choixSommet(G, "un nouveau sommet de depart")-1
            input("\nCliquer sur Enter pour choisir un autre graph : ")
    else: val = len(graphs)
