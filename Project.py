import os

# Récupère le répertoire de tous les graphiques situés dans le répertoire des programmes.
dir = os.path.split(__file__)[0]

Extentions = ['.txt', '.TXT']
inf = float('inf')


# Lit un graphique dans le répertoire en utilisant son nom de fichier
def readGraph(filedir):
    file = open(filedir)
    size = int(file.readline().split()[0])
    nbArc = int(file.readline().split()[0])
    # Tout les sommets sont initialisés a 'inf'
    mat = [[float('inf')] * int(size) for i in range(int(size))]
    for i in range(int(size)): mat[i][i] = '0'
    for i in range(nbArc):
        line = file.readline().split()
        n = int(line[0])
        m = int(line[1])
        mat[n][m] = float(line[2])
    return nbArc, size, mat


# Affichage normalisé du graph
def printGraph(graph):
    print("Sommet ", end='', flush=True)
    for i in range(graph[1]):
        print("   " + str(i) + "     ", end='', flush=True)
    print("")
    for i in range(graph[1]):
        print(" " + str(i) + " :   ", end='', flush=True)
        for j in range(graph[1]):
            print("[  " + str(graph[2][i][j]) + " " * (5 - len(str(graph[2][i][j]))) + "]", end="", flush=True)
        print()


# Fonction qui affiche le menu et la liste des graphes
def choixGraph(graphList):
    print("Choisissez le graph a traiter : ")
    for i in range(len(graphList)):
        print(str(i + 1) + ") Graph [" + graphList[i][3][:-4] + "] =<S,A> / Cardinalité(S) = " + str(
            graphList[i][1]) + " / Cardinalité(A) = " + str(graphList[i][0]) + ".")
    print("\t [0] Pour quitter.")
    val = int(input("\t   Votre choix : "))
    if (val < 0 or val > len(graphList)): print("\n\n[Veuillez effectuer un choix valide...]\n\n")
    return val


graphs = []


# Fonction qui converti une matrice d'adjacense a un tuple de (listSommets, listArcs)
def convert(matrix):
    vertices = list(range(len(matrix)))
    edges = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != float('inf'):
                edges.append((i, j, matrix[i][j]))
    return vertices, edges


# Implémentation de l'algorithme de Floyd Warshall
def floyd(vertices, edges):
    negative = False
    dist = [[float("inf")] * len(vertices) for i in range(len(vertices))]
    nxt = [[None] * len(vertices) for i in range(len(vertices))]
    # Initialisation des Matrices
    for edge in edges:
        u, v, w = edge
        dist[u][v] = w
        nxt[u][v] = v
    for v in vertices:
        dist[v][v] = 0
        nxt[v][v] = v
    for k in range(len(vertices)):
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if (i == j and dist[i][j] < 0):
                    # Détection de cycle absorbant
                    negative = True
                    break
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]
                    print("\n\tMatrice des distances les plus court entre chaque sommet iteration " + str(k) + " : ")
                    printGraph((0, len(dist), dist))
                    print("\n\tMatrice des successeurs iteration " + str(k) + " : ")
                    printGraph((0, len(nxt), nxt))
    return dist, nxt, negative


# Utilise la matrice des successeurs pour construire le chemain le plus court entre 2 sommets
def get_path(nxt, u, v):
    if nxt[u][v] is None:
        return None
    path = [u]
    while u != v:
        u = nxt[u][v]
        path.append(u)
    return path


# Utilisation de readGraph pour charger tout les graphes en memoire d'apres leur fichier
for file in os.listdir(dir):
    if (file[-4:] in Extentions):
        nbArc, size, mat = readGraph(dir + '/' + file)
        vertices, edges = convert(mat)
        dist, nxt = floyd(vertices, edges)
        print(get_path(nxt, 2, 0))
        """graphs.append((nbArc, size, mat, file))"""

val = len(graphs)

# implémentation de l'algorithme
"""def floydWarshall(Graph):
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
    return P,cycleABS,D"""

# Boucle pour continuer a traiter n graphes tantque l'utilisateur ne choisis pas de quitter
"""while (val > 0 and val <= len(graphs)): 
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
    else: val = len(graphs)"""
