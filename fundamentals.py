import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()
Gd = nx.DiGraph()
Gm = nx.MultiGraph()
Gmd = nx.MultiDiGraph()

# # ------------------------------- MANUALLY ADDING ------------------------------------------

# G.add_edge(1,2)
# G.add_edge(2,3, weight = 0.9)
# G.add_edge("A","B")
# G.add_edge("4","4")
# G.add_node(print)
# G.add_node("C")
# nx.draw_spring(G, with_labels = True)
# plt.show()

# # ------------------- ADDING EDGES FROM A LIST ----------------------------------

# edges = [(1,2),(2,3),("A","B"),("4","4"),("A", "C")]
# Gd.add_edges_from(edges)
# nx.draw_spring(G, with_labels = True)
# # plt.show()

# # # ADJACENCY MATRIX

# print(nx.adjacency_matrix(G))
# plt.show()

# # ----------------- ADDING FROM ADJACENCY MATRIX --------------------------

# G = nx.from_numpy_array(np.array([[0,1,0],[1,0,0],[1,1,0]]))

# nx.draw_spring(G, with_labels = True)
# plt.show()

# print(nx.adjacency_matrix(G))
# plt.show()

## ----------------------------------------- VISUALISATIONS ----------------------------------------

# G = nx.from_numpy_array(np.array([[0,1,0],[1,0,0],[1,1,0]]))

# nx.draw_spectral(G, with_labels = True)
# plt.show()

# print(nx.adjacency_matrix(G))
# plt.show()

## ------------------------- COMPLETE GRAPH ---------------------------------

# Gd = nx.complete_graph(4)

# # ------------------------- DEGREE ---------------------------------

# print(dict(Gd.in_degree)["B"])

# nx.draw(Gd, with_labels = True)

# plt.show()


# # ---------------------- SHORTEST PATH -------------------------------------

# edges = [(1,2),(2,3),(3,5),(4,6),(3,4),(6,7), (2,8),(8,9),(9,4)]
# G.add_edges_from(edges)
# nx.draw_planar(G, with_labels = True)

# print(nx.shortest_path_length(G,1,3))
# plt.show()
