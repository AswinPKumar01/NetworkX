# Types of Graphs:

- G = nx.Graph()
- Gd = nx.DiGraph()
- Gm = nx.MultiGraph()
- Gmd = nx.MultiDiGraph()


# Add nodes/ edges:

- G.add_edge / G.add_node
- G.add_edges_from(list)
- FROM ADJACENCY LIST:
  nx.from_numpy_array(array)

# Visualizations:

- draw_spring()
- draw_circular() : Arranges in circular way
- draw_shell() : Concentric Circles
- draw_spectral() : 
- draw_random(): Randomly
- draw_planar(): Edges doesnt intersect


# Degree:
- dict(G.degree)[node_name]
- dict(G.in_degree)[node_name]
- dict(G.out_degree)[node_name]


# Shotest Path:
- nx.shortest_path(G,edge1,edge2)
- nx.shortest_path_length(G,edge1,edge2)
