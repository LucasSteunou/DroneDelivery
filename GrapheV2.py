#!/usr/bin/env python
from time import time
import json
import math as m
from tqdm import tqdm
import random as rd
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from scipy.sparse import lil_matrix
from networkx.algorithms import tournament

## Excel, découpage,...
data = pd.read_csv(r"C:\Users\steun\Desktop\TIPE\filaire-de-voirie.csv", sep=";")
T = pd.DataFrame(data, columns=["Geo Shape", "longueur"])

# Remove rows with NaN values in the 'Geo Shape' column
T.dropna(subset=["Geo Shape"], inplace=True)

# Convert JSON strings to dictionaries
T["Geo Shape"] = T["Geo Shape"].apply(json.loads)
# geo shape type: dict with key ['coordinates', 'type'].
# 'type' is the same for all, so we remove it and only keep the coordinates
# coordinates are one element lists, so we take item 0
T["Geo Shape"] = T["Geo Shape"].apply(
    lambda x: x["coordinates"][0]
    if isinstance(x, dict) and "coordinates" in x
    else None
)

# Convert "Geo Shape" column to a NumPy array
geo_shapes = np.array(T["Geo Shape"])

# Extract first and last coordinates from each row
first_coords = [shape[0] for shape in geo_shapes]
last_coords = [shape[-1] for shape in geo_shapes]

# Create the list F
F = [
    [first, last, length]
    for first, last, length in zip(first_coords, last_coords, T["longueur"])
]

C = []  # Juste les coordonnées des sommets
print("Getting coordinates...")

C = []
coordinate_set = set()  # Set to store unique coordinates

for line in F:
    start_coord, end_coord, length = line[0], line[1], line[2]

    start_coord_tuple = tuple(start_coord)
    if start_coord_tuple not in coordinate_set:
        C.append(start_coord)
        coordinate_set.add(start_coord_tuple)

    end_coord_tuple = tuple(end_coord)
    if end_coord_tuple not in coordinate_set:
        C.append(end_coord)
        coordinate_set.add(end_coord_tuple)

n = len(C)

# Compute the adjacency matrix M and angle matrix A
A = lil_matrix((n, n))
M = lil_matrix((n, n))


print("Cleaning matrix...")


def signe(a, b):
    if b > a:
        return 1
    else:
        return -1


coord_to_index = {tuple(coord): index for index, coord in enumerate(C)}


for i in F:
    a = coord_to_index[tuple(i[0])]
    b = coord_to_index[tuple(i[1])]

    if a != b:  # Routes qui font des boucles??
        M[a, b] = i[2]
        M[b, a] = i[2]
        if C[b][0] - C[a][0] > 0:
            A[a, b] = m.atan((C[b][1] - C[a][1]) / (C[b][0] - C[a][0]))
            A[b, a] = m.atan((C[b][1] - C[a][1]) / (C[b][0] - C[a][0])) + m.pi
        if C[b][0] - C[a][0] < 0:
            A[a, b] = m.atan((C[b][1] - C[a][1]) / (C[b][0] - C[a][0])) + m.pi
            A[b, a] = m.atan((C[b][1] - C[a][1]) / (C[b][0] - C[a][0]))
        if C[b][0] - C[a][0] == 0:
            A[a, b] = signe(C[a][1], C[b][1]) * m.pi / 2
            A[b, a] = signe(C[b][1], C[a][1]) * m.pi / 2

# needed to be faster
A = A.tocsr()
M = M.tocsr()

# Affichage
P = [k for k in range(n)]
G = nx.Graph()
G.add_nodes_from(P)
D = []
print("Creating visualization...")
rows, cols = M.nonzero()
for i, j in zip(rows, cols):
    if i <= j:
        G.add_edge(i, j, weight=M[i, j])


labels_edges = {}
print("Matching labels and edges...")
labels_edges = {edge: G.edges[edge]["weight"] for edge in G.edges}
posi = {}
for k in P:
    posi[k] = C[k]

nx.draw_networkx_edges(G, posi,width=0.7)
print("Done!")




##
J=nx.Graph()
J.add_nodes_from([16362])
posito={}
for i in [16362]:
    posito[i]=C[i]
nx.draw_networkx_nodes(J,posito,node_size=100)

plt.show()


