def astar(G,L): #G nx.graph, L=[sommet1, S2,...,Sk]
    k=len(L)
    B=[[0 for i in range(k)] for j in range(k)]
    nx.draw_networkx_edges(G,posi,width=0.6)
    for i in tqdm(range(k)):
        for j in range(i+1,k):
            longueur= nx.astar_path_length(G,L[i],L[j])
            B[i][j] = longueur
            B[j][i] = longueur
            Chemin=nx.astar_path(G,L[i],L[j])
            Gr=nx.Graph()
            Gr.add_nodes_from(Chemin)
            position={}
            for l in Chemin:
                position[l]=C[l]

            E=[]
            for l in range(len(Chemin)-1):
                E.append((Chemin[l],Chemin[l+1],M[Chemin[l],Chemin[l+1]]))
            Gr.add_weighted_edges_from(E)
            labels = {}
            labels = {edge:Gr.edges[edge]['weight'] for edge in Gr.edges}
            S=nx.Graph()
            S.add_nodes_from(L)
            position2={}
            for l in L:
                position2[l]= C[l]
            nx.draw(S,position2,node_size=200)
            nx.draw_networkx_edges(Gr,position,edge_color='r',width=2)

    return B


##
import random as rd
L=[rd.randrange(n) for i in range(6)]
B= astar(G,L)
S=nx.Graph()
S.add_nodes_from(L)
position={}
for i in L:
    position[i]= C[i]
nx.draw(S,position,node_size=200)
##
plt.show()

##Algos V2
def puissance(Masse):
    return 4*((Masse*g/4)**3/(2*pi*rho*R**2))**(1/2)


#Gc graphe complet
def energie_chemin(Gc,chemin,colis): #chemin=[sommet dép, S1,S2,...,Sn-1], P=[0,m1,...,mn-1]
    N=len(Gc)
    masse=masse_drone+sum(colis)
    E=0
    i=0
    while i < N-1:
        E += puissance(masse)*Gc[chemin[i]][chemin[i+1]]/Vitesse_moy
        masse -= colis[i+1]
        i += 1
    E += puissance(masse)*Gc[chemin[N-1]][0]/Vitesse_moy
    return E/Etot

#d=[rd.randrange(n)] #Point de départ (entrepôt)
def permutations(perm,deb,fin=[]): #deb = liste des sommets sans le point de départ
    if len(deb)== 0:
        perm.append([0] + fin)
    else:
        for i in range(len(deb)):
            permutations(perm,deb[:i] + deb[i+1:], fin + deb[i:i+1])

def chemin_opti(Gc,colis):
    Min=energie_chemin(Gc,[k for k in range(len(Gc))],colis)  #chemin [0,1,2,3,...,n-1] de référence
    ChemOpti=[k for k in range(len(Gc))]
    Perm=[]
    permutations(Perm,[k for k in range(1,len(Gc))])
    for chemin in tqdm(Perm):
        if energie_chemin(Gc,chemin,colis) < Min:
            Min = energie_chemin(Gc,chemin,colis)
            ChemOpti= chemin
    return [ChemOpti,Min]

##Affiche sommets avec masses
# Création colis, sommets...
plt.clf()
t=time()
d=[18484]  # départ
k=6  # Nbre de colis, à partir de 11 ça devient très long (25 min)
sommets=[rd.randrange(n) for _ in range(k)]
print('Creation du graphe complet...')
Gc=astar(G,d+sommets)
colis=[rd.randint(1,int(masse/k+1))+rd.randint(0,10)/10 for _ in range(k)] #moyenne de la somme ~ autour de masse
colis=[0] + colis
# Affichage masses
def kg(i):
    return str(i) + 'kg'
Colis=[kg(i) for i in colis[1:]]
Gm=nx.Graph()
Colis.append('Dép')
Gm.add_nodes_from(Colis)
position3={}
position3['Dép']=C[d[0]]
for i in colis:
    position3[str(i)+'kg'] = C[(d+sommets)[colis.index(i)]]
nx.draw(Gm,position3,node_size=400,with_labels=True,font_size=7)
plt.show()

##Affiche chemin opti
print('Recherche du chemin optimal...')
Gc=astar(G,d+sommets)
CHO=chemin_opti(Gc,colis)
ChemOpti=CHO[0]
Min=CHO[1]

S=nx.Graph()
S.add_nodes_from([k for k in range(len(Gc))])
position={}
position[0]=C[d[0]]
for i in range(1,len(Gc)):
    position[i]= C[sommets[ChemOpti[i]-1]]

nx.draw(S,position,node_size=200,with_labels=True)

print('Ordre optimal:',ChemOpti,', Energie depensée:',Min*100,'% de Etotale')
print('Terminé en',int(time()-t),'s!')


##Comparaison avec chemin le plus court
def longueur_chemin(Gc,chemin):
    l=0
    N=len(Gc)
    i=0
    while i < N-1:
        l += Gc[chemin[i]][chemin[i+1]]
        i+=1
    l += Gc[chemin[N-1]][0]
    return l

def chemin_court(Gc):
    ChemCourt=[k for k in range(len(Gc))]
    Lmin=longueur_chemin(Gc,ChemCourt)
    Perm=[]
    permutations(Perm,[k for k in range(1,len(Gc))])
    for chemin in Perm:
            if longueur_chemin(Gc,chemin) < Lmin:
                Lmin=longueur_chemin(Gc,chemin)
                ChemCourt=chemin
    return [ChemCourt,Lmin]

print('Recherche chemin le plus court...')
t=time()
Gc=astar(G,d+sommets)
CHC=chemin_court(Gc)
ChemCourt=CHC[0]
Lmin=CHC[1]
#plt.show() #à mettre si on veut voir sans l'ordre
Sc=nx.Graph()
Sc.add_nodes_from([k for k in range(len(Gc))])
position2={}
position2[0]=C[d[0]]
for i in range(1,len(Gc)):
    position2[i]= C[sommets[ChemCourt[i]-1]]

nx.draw(Sc,position2,node_size=200,with_labels=True)
Ec=energie_chemin(Gc,ChemCourt,colis)
print('Ordre court:',ChemCourt,', Energie depensee:',Ec*100,'% de Etotale')
print('Terminé en',int(time()-t),'s!')
plt.show()

##Moyenne gain énergie /chemin court
# Enlever affichage avant
k=11
LOpti=[]
LCourt=[]
for _ in tqdm(range(100)):
    sommets=[rd.randrange(n) for _ in range(k)]
    try:
        Gc=astar(G,d+sommets)
        colis=[rd.randint(1,2*int(masse/k+1)) for _ in range(k)]
        colis=[0] + colis
        Opti=chemin_opti(Gc,colis)[1]
        Court=energie_chemin(Gc,chemin_court(Gc)[0],colis)
        LOpti.append(Opti)
        LCourt.append(Court)
    except:
        pass
print('Moyenne opti =',sum(LOpti)/len(LOpti))
print('Moyenne court =',sum(LCourt)/len(LCourt))

#90% court, 83% opti pour k=6 (9 erreurs de noeud innateignable sur les 100), colis int(masse/k+1)
#97% court, 90% opti pour k=7 (5 erreurs de noeud innateignable sur les 100)
#1.03% court, 95% opti pour k=8 (9 erreurs de noeud innateignable sur les 100)
#k=9, colis 2*int(masse/k+1): 1.55% court, 1.39 opti (8 erreurs)



##Erreurs (sommets innateignables)
a=0
E=[]
for i in tqdm(range(n)): #45 min
    try:
        l=nx.astar_path_length(G,d[0],i)
    except:
        a+=1
        E.append(i)

##
erreurs=[38, 39, 174, 175, 227, 228, 293, 294, 623, 624, 1366, 1367, 2023, 2024, 2042, 2043, 2458, 2459, 2558, 2559, 2725, 2726, 3337, 3338, 3531, 3532, 4502, 4503, 4505, 4842, 4843, 4928, 4929, 5592, 5593, 5795, 5796, 5877, 5878, 5995, 5996, 6244, 6245, 6333, 6334, 6518, 6519, 7078, 7079, 7472, 7473, 7881, 7882, 8082, 8083, 8084, 8085, 8427, 8487, 8488, 9391, 9392, 9393, 9406, 9407, 9509, 9583, 9584, 9771, 9772, 9778, 9779, 9809, 9810, 9847, 9848, 9849, 10341, 10342, 10506, 10507, 10508, 10903, 10904, 10905, 10906, 10957, 10958, 11035, 11036, 11435, 11463, 11464, 11476, 11477, 11517, 11518, 11533, 11650, 11657, 11658, 11777, 11778, 11845, 11846, 12140, 12141, 12185, 12214, 12215, 12231, 12232, 12250, 12251, 12306, 12499, 12566, 12567, 12574, 12575, 12583, 12584, 12780, 12781, 13269, 13270, 13415, 13416, 13440, 13441, 13622, 13623, 13681, 14337, 14367, 14368, 14571, 14572, 14694, 14782, 14783, 14954, 14955, 15015, 15154, 15155, 15283, 15284, 15741, 15742, 15846, 15847, 15914, 16178, 16179, 16204, 16205, 16653, 16654, 16692, 16768, 16769, 17228, 17229, 17396, 17397, 17561, 17562, 17580, 17700, 17701, 17707, 17708, 17923, 17924, 17971, 17972, 18150, 18151, 18228, 18251, 18338, 18385, 18386, 18437, 18438, 18456, 18457, 18814, 18815, 18876, 18877, 18913, 18914, 19034, 19035, 19060, 19061, 19230, 19231, 19248, 19300, 19301, 19311, 19312, 19332, 19333, 19585, 19783, 19784, 20174, 20175, 20260, 20261, 20288, 20289, 20359, 20376, 20682, 20880, 20881, 20976, 20996, 20997, 21306, 21307, 21530, 21531, 21561, 21562, 21689, 21690, 21705, 21706, 21763, 21798, 21799, 21847, 21907, 21926, 21927, 21932, 21933, 21942, 21943, 21995, 22000, 22048, 22049, 22102, 22153, 22154, 22174, 22175, 22237, 22238, 22264, 22265, 22282, 22303, 22362, 22363, 22396, 22397, 22450, 22451, 22523, 22526, 22527, 22563, 22564, 22583, 22584, 22703, 22864, 22865, 23057, 23180, 23385, 23421, 23567, 23568, 23631, 23708, 23709, 23716, 23725, 23730, 23734, 23735, 23753, 23754, 23758, 23780, 23781, 23838, 23876, 23877, 23888, 23904, 23905, 23929, 23930, 24040, 24041, 24073, 24074, 24192, 24193, 24244, 24248, 24249, 24333, 24334, 24377, 24378, 24425, 24448, 24449, 24482, 24483, 24489, 24524, 24575, 24576, 24667, 24668]


##
G2=nx.Graph()
C2=[]
L2=[]
for i in tqdm(C):  # C= Liste des coordonnées de toutes les intersections de Toulouse
    if i[0] > 1.399145 and i[0] < 1.503258 and i[1] > 43.573202 and i[1] < 43.617040:
        C2.append(i)
        L2.append(C.index(i))
G2.add_nodes_from(L2)
posito3={}
for i in L2:
    posito3[i]=C[i]
rows, cols = M.nonzero()   # M= Matrice d'adjacence de Toulouse (Matrice creuse)
for i, j in zip(rows, cols):
    if i <= j:
        if i in L2 and j in L2:
            G2.add_edge(i, j, weight=M[i, j])
labels_edges = {}
labels_edges = {edge: G2.edges[edge]["weight"] for edge in G2.edges}

bg=[1.399145, 43.573202]  # Coins du rectangle de la photo
hd=[1.503258, 43.617040]
hg=[1.399145, 43.617040]
bd=[1.503258, 43.573202]

colis=['Départ','5 kg', '0.5 kg', '0.1 kg', '1 kg']
J=nx.Graph()
J.add_nodes_from(colis)
posito={}
coord=[[1.475334438274966, 43.57870959790727], [1.426947462227057, 43.60792337544156], [1.447025719178776, 43.596436979947015], [1.478582454254292, 43.605983760146], [1.414944282469067, 43.583407610802695]]  # Coordonnées sommets à livrer
for i in colis:
    posito[i]=coord[colis.index(i)]
plt.clf()
nx.draw(J,posito, with_labels=True, node_size=1800, node_color='#FFCA08') #Tracé des sommets (masses)
nx.draw_networkx_edges(G2, posito3, width=0.9)   # Tracé des routes de Toulouse

L=[C.index(i) for i in coord]
B=completion(M,L)  # Tracé du plus court chemin pour chaque couple

##
Colis=[0,5,0.5,0.1,1]
CHO=chemin_opti(B,Colis)
ChemOpti=CHO[0]

S=nx.Graph()
S.add_nodes_from([k for k in range(1,len(B))])
S.add_node('Départ')
position={}
position['Départ']=[1.475334438274966, 43.57870959790727]
for i in range(1,len(B)):
    position[i]= coord[ChemOpti[i]]

nx.draw(S,position,node_size=1800,with_labels=True, node_color='#FFCA08') # Tracé de l'ordre optimal

plt.show()





