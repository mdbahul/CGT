# from itertools import combinations

# # Function for Depth First Search (DFS)
# def dfs(graph, vertex, visited):
#     visited.add(vertex)
#     for neighbor in graph[vertex]:
#         if neighbor not in visited:
#             dfs(graph, neighbor, visited)

# # Function to check if the graph is connected
# def is_connected(graph):
#     vertices = list(graph.keys())
#     visited = set()

#     # Start DFS from the first vertex
#     dfs(graph, vertices[0], visited)

#     # If all vertices are visited, the graph is connected
#     return len(visited) == len(vertices)

# # Function to remove vertices from the graph
# def remove_vertices(graph, vertices_to_remove):
#     new_graph = {}
#     for vertex, neighbors in graph.items():
#         if vertex not in vertices_to_remove:
#             new_graph[vertex] = [n for n in neighbors if n not in vertices_to_remove]
#     return new_graph

# # Function to remove edges from the graph
# def remove_edges(graph, edges_to_remove):
#     new_graph = {}
#     for vertex, neighbors in graph.items():
#         new_neighbors = []
#         for neighbor in neighbors:
#             if (vertex, neighbor) not in edges_to_remove and (neighbor, vertex) not in edges_to_remove:
#                 new_neighbors.append(neighbor)
#         new_graph[vertex] = new_neighbors
#     return new_graph

# # Function to calculate vertex connectivity
# def vertex_connectivity(graph):
#     vertices = list(graph.keys())
#     n = len(vertices)
    
#     # Start with removing 1 vertex, 2 vertices, ..., (n-1) vertices
#     for k in range(1, n):
#         for subset in combinations(vertices, k):
#             new_graph = remove_vertices(graph, subset)
#             if not is_connected(new_graph):
#                 return k, list(subset)

#     return n - 1, []

# # Function to calculate edge connectivity
# def edge_connectivity(graph):
#     edges = []
#     for vertex, neighbors in graph.items():
#         for neighbor in neighbors:
#             if (vertex, neighbor) not in edges and (neighbor, vertex) not in edges:
#                 edges.append((vertex, neighbor))

#     # Start with removing 1 edge, 2 edges, ..., len(edges) edges
#     for k in range(1, len(edges) + 1):
#         for subset in combinations(edges, k):
#             new_graph = remove_edges(graph, subset)
#             if not is_connected(new_graph):
#                 return k, list(subset)

#     return len(edges), []

# # Sample graph as adjacency list (without weights)
# graph = {4: {3: 10, 2: 7, 1: 8, 0: 9}, 3: {4: 10, 2: 8, 1: 9, 0: 8}, 2: {4: 7, 3: 8, 1: 6, 0: 3}, 1: {4: 8, 3: 9, 2: 6, 0: 7}, 0: {4: 9, 3: 8, 2: 3, 1: 7}}

# # Find vertex connectivity
# vertex_conn_value, vertices_removed = vertex_connectivity(graph)
# print(f"Vertex Connectivity: {vertex_conn_value}")
# print(f"Vertices to remove to disconnect the graph: {vertices_removed}")

# # Find edge connectivity
# edge_conn_value, edges_removed = edge_connectivity(graph)
# print(f"Edge Connectivity: {edge_conn_value}")
# print(f"Edges to remove to disconnect the graph: {edges_removed}")

# # K-connected graph is based on vertex connectivity
# K_connected = vertex_conn_value
# print(f"The graph is {K_connected}-connected.")


# Function for Depth First Search (DFS)
def dfs(graph, vertex, visited):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Function to check if the graph is connected
def is_connected(graph):
    vertices = list(graph.keys())
    visited = set()

    # Start DFS from the first vertex
    dfs(graph, vertices[0], visited)

    # If all vertices are visited, the graph is connected
    return len(visited) == len(vertices)

# Function to remove vertices from the graph
def remove_vertices(graph, vertices_to_remove):
    new_graph = {}
    for vertex, neighbors in graph.items():
        if vertex not in vertices_to_remove:
            new_graph[vertex] = {n: w for n, w in neighbors.items() if n not in vertices_to_remove}
    return new_graph

# Function to remove edges from the graph
def remove_edges(graph, edges_to_remove):
    new_graph = {}
    for vertex, neighbors in graph.items():
        new_neighbors = {}
        for neighbor, weight in neighbors.items():
            if (vertex, neighbor) not in edges_to_remove and (neighbor, vertex) not in edges_to_remove:
                new_neighbors[neighbor] = weight
        new_graph[vertex] = new_neighbors
    return new_graph

# Function to calculate vertex connectivity
def vertex_connectivity(graph):
    vertices = list(graph.keys())
    n = len(vertices)

    # Try removing k vertices and checking connectivity
    for k in range(1, n):
        from itertools import combinations
        for vertices_to_remove in combinations(vertices, k):
            new_graph = remove_vertices(graph, vertices_to_remove)
            if not is_connected(new_graph):
                return k, vertices_to_remove

    return n - 1, []

# Function to calculate edge connectivity
def edge_connectivity(graph):
    edges = []
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            if (vertex, neighbor) not in edges and (neighbor, vertex) not in edges:
                edges.append((vertex, neighbor))

    # Try removing k edges and checking connectivity
    for k in range(1, len(edges) + 1):
        from itertools import combinations
        for edges_to_remove in combinations(edges, k):
            new_graph = remove_edges(graph, edges_to_remove)
            if not is_connected(new_graph):
                return k, edges_to_remove

    return len(edges), []

# Input graph (weighted adjacency list)
graph = {
    0: {1: 1, 2: 1, 3: 1, 4: 1},
    1: {0: 1},
    2: {0: 1},
    3: {0: 1},
    4: {0: 1}
}

# Find vertex connectivity
vertex_conn_value, vertices_removed = vertex_connectivity(graph)
print(f"Vertex Connectivity: {vertex_conn_value}")
print(f"Vertices to remove to disconnect the graph: {vertices_removed}")

# Find edge connectivity
edge_conn_value, edges_removed = edge_connectivity(graph)
print(f"Edge Connectivity: {edge_conn_value}")
print(f"Edges to remove to disconnect the graph: {edges_removed}")
