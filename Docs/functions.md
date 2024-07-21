# NetworkX Fundamentals

Key aspects of the NetworkX library, including graph types, node and edge management, visualizations, degree calculations, shortest path algorithms, centrality measures, and more in a nutshell.

Full Documentation can be accessed <a href = "https://networkx.org/documentation/stable/index.html" target = "blank">here.<a/>

## Table of Contents

1. [Graph Types](#graph-types)
2. [Adding Nodes and Edges](#adding-nodes-and-edges)
3. [Visualizations](#visualizations)
4. [Degree](#degree)
5. [Shortest Path](#shortest-path)
6. [Centrality Measures](#centrality-measures)
7. [Density](#density)
8. [Diameter](#diameter)
9. [Eulerian Path](#eulerian-path)
10. [Cliques](#cliques)
11. [Bridges](#bridges)
12. [Connected Components](#connected-components)

## Graph Types

NetworkX supports various graph types to suit different needs:

- **Undirected Graph**
  ```python
  G = nx.Graph()
  ```
  Represents a graph where edges have no direction.

- **Directed Graph**
  ```python
  Gd = nx.DiGraph()
  ```
  Represents a graph where edges have a direction.

- **Undirected Graph with Multiple Edges**
  ```python
  Gm = nx.MultiGraph()
  ```
  Allows multiple edges between nodes.

- **Directed Graph with Multiple Edges**
  ```python
  Gmd = nx.MultiDiGraph()
  ```
  Allows multiple directed edges between nodes.

## Adding Nodes and Edges

- **Add a Single Node**
  ```python
  G.add_node(node)
  ```

- **Add Multiple Nodes**
  ```python
  G.add_nodes_from([node1, node2, node3])
  ```

- **Add a Single Edge**
  ```python
  G.add_edge(node1, node2)
  ```

- **Add Multiple Edges**
  ```python
  G.add_edges_from([(node1, node2), (node2, node3)])
  ```

- **From Adjacency List**
  Convert an adjacency matrix or list to a NetworkX graph:
  ```python
  G = nx.from_numpy_array(array)
  ```

## Visualizations

Visualizing graphs helps in understanding their structure and properties:

- **Spring Layout**: Forces-directed layout
  ```python
  nx.draw_spring(G)
  ```

- **Circular Layout**: Arranges nodes in a circle
  ```python
  nx.draw_circular(G)
  ```

- **Shell Layout**: Arranges nodes in concentric circles
  ```python
  nx.draw_shell(G)
  ```

- **Spectral Layout**: Based on the eigenvectors of the graph Laplacian
  ```python
  nx.draw_spectral(G)
  ```

- **Random Layout**: Randomly positions nodes
  ```python
  nx.draw_random(G)
  ```

- **Planar Layout**: Ensures edges do not intersect
  ```python
  nx.draw_planar(G)
  ```

## Degree

The degree of a node indicates its connectivity:

- **Degree of a Node**
  ```python
  dict(G.degree)[node_name]
  ```

- **In-Degree (for Directed Graphs)**
  ```python
  dict(G.in_degree)[node_name]
  ```

- **Out-Degree (for Directed Graphs)**
  ```python
  dict(G.out_degree)[node_name]
  ```

## Shortest Path

Find the shortest path between nodes:

- **Shortest Path**
  ```python
  nx.shortest_path(G, source=node1, target=node2)
  ```

- **Shortest Path Length**
  ```python
  nx.shortest_path_length(G, source=node1, target=node2)
  ```

## Centrality Measures

Centrality measures assess the importance of nodes in a graph:

- **Degree Centrality**
  ```python
  nx.degree_centrality(G)
  ```

- **Betweenness Centrality**
  ```python
  nx.betweenness_centrality(G)
  ```

- **Closeness Centrality**
  ```python
  nx.closeness_centrality(G)
  ```

- **Eigenvector Centrality**
  ```python
  nx.eigenvector_centrality(G)
  ```

- **PageRank**
  ```python
  nx.pagerank(G)
  ```

## Density

Graph density measures how close the graph is to being a complete graph:

- **Density of a Graph**
  ```python
  nx.density(G)
  ```

## Diameter

The diameter of a graph is the longest shortest path between any two nodes:

- **Diameter**
  ```python
  nx.diameter(G)
  ```

  Note: Diameter is only defined for connected graphs.

## Eulerian Path

An Eulerian Path visits every edge exactly once:

- **Check for Eulerian Path**
  ```python
  nx.has_eulerian_path(G)
  ```

- **Find Eulerian Path**
  ```python
  path = nx.eulerian_path(G)
  ```

  Note: An Eulerian Path exists if and only if the graph is connected and has exactly zero or two nodes of odd degree.

## Cliques

Cliques are subsets of nodes such that every two nodes are connected:

- **Find All Cliques**
  ```python
  cliques = list(nx.find_cliques(G))
  ```

- **Find Maximal Clique**
  ```python
  largest_clique = max(nx.find_cliques(G), key=len)
  ```

## Bridges

Bridges are edges whose removal increases the number of connected components:

- **Find Bridges**
  ```python
  bridges = list(nx.bridges(G))
  ```

## Connected Components

Connected components are maximal subgraphs where any two nodes are connected:

- **Find Connected Components**
  ```python
  components = list(nx.connected_components(G))
  ```

- **Number of Connected Components**
  ```python
  num_components = nx.number_connected_components(G)
  ```

This guide provides an overview of essential NetworkX functionalities. For more details and advanced features, refer to the [NetworkX Documentation](https://networkx.org/documentation/stable/).
