import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import heapq
import random
random.seed(42)

def deg_seq_to_dict(degree_sequence):
    # Check if the sum of degrees is even (necessary condition for a graphical sequence)
    if sum(degree_sequence) % 2 != 0:
        raise ValueError("The degree sequence is not graphical (sum of degrees must be even).")
    
    # Initialize an empty adjacency list for the graph
    graph = defaultdict(list)
    
    # Assign node labels from 0 to len(degree_sequence) - 1
    nodes = list(range(len(degree_sequence)))
    
    # Work on a sorted version of the degree sequence
    degree_sequence = sorted(zip(degree_sequence, nodes), reverse=True)  # (degree, node)
    
    # While there are remaining degrees
    while degree_sequence:
        # Sort by the remaining degrees in descending order
        degree_sequence.sort(reverse=True, key=lambda x: x[0])

        # Get the node with the highest degree
        degree, node = degree_sequence.pop(0)
        
        if degree > len(degree_sequence):
            raise ValueError("The degree sequence is not graphical (too few nodes left to satisfy the degree).")
        
        # Connect this node to the next highest-degree nodes
        for i in range(degree):
            graph[node].append(degree_sequence[i][1])
            graph[degree_sequence[i][1]].append(node)
            # Reduce their degree by 1
            degree_sequence[i] = (degree_sequence[i][0] - 1, degree_sequence[i][1])
        
        # Remove nodes whose degree is now 0
        degree_sequence = [(d, n) for d, n in degree_sequence if d > 0]
    
    return dict(graph)


def is_valid_next_edge(graph, u, v):
    # Check if the edge u-v is valid to traverse
    if len(graph[u]) == 1:
        return True
    else:
        # Check if it's a bridge by using DFS (depth-first search) to count components
        original_component_count = count_components(graph, u)
        
        # Temporarily remove the edge
        graph[u].remove(v)
        graph[v].remove(u)
        
        # Recalculate components after removing the edge
        new_component_count = count_components(graph, u)
        
        # Restore the edge back
        graph[u].append(v)
        graph[v].append(u)
        
        # Check if it was a bridge
        return original_component_count == new_component_count


def count_components(graph, u):
    visited = set()
    
    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
    
    # Start DFS from the given node u
    dfs(u)
    return len(visited)


def find_eulerian_path(graph):
    # Copy the graph to avoid modifying the original graph
    graph_copy = {node: neighbors[:] for node, neighbors in graph.items()}
    
    # Find a starting point (for Eulerian or semi-Eulerian graph)
    start_node = None
    odd_degree_nodes = [node for node in graph_copy if len(graph_copy[node]) % 2 == 1]
    
    if len(odd_degree_nodes) == 0:
        # Eulerian circuit: start from any node
        start_node = list(graph_copy.keys())[0]
    elif len(odd_degree_nodes) == 2:
        # Semi-Eulerian path: start from one of the odd-degree nodes
        start_node = odd_degree_nodes[0]
    else:
        return "The graph is not Eulerian or semi-Eulerian."
    
    # Fleury's algorithm to find the Eulerian path
    path = []
    def fleury(u):
        while graph_copy[u]:
            v = graph_copy[u][0]
            if is_valid_next_edge(graph_copy, u, v):
                # Remove the edge from the graph
                graph_copy[u].remove(v)
                graph_copy[v].remove(u)
                
                # Traverse this edge
                path.append((u, v))
                fleury(v)
    
    # Start traversal from the start node
    fleury(start_node)
    return path

# Function to assign random weights to edges
def assign_random_weights(graph):
    weighted_graph = {}
    
    for node, neighbors in graph.items():
        weighted_graph[node] = {}
        for neighbor in neighbors:
            if neighbor not in weighted_graph:  # Initialize neighbor's dictionary
                weighted_graph[neighbor] = {}
                
            # Assign a random weight to the edge (node, neighbor) and (neighbor, node)
            if neighbor not in weighted_graph[node]:  # Only assign if not already assigned
                weight = random.randint(1, 10)  # You can change the range as needed
                weighted_graph[node][neighbor] = weight
                weighted_graph[neighbor][node] = weight  # Same weight for reverse direction

    return weighted_graph

# Dijkstra's algorithm implementation
def dijkstra(graph, start):
    # Step 1: Initialization
    # Set initial distances to infinity, and the distance to the start node as 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to get the node with the smallest distance
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Step 2: Visit node with smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Step 3: Skip processing if we already found a shorter path
        if current_distance > distances[current_node]:
            continue
        
        # Step 4: Calculate tentative distances to neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Step 5: Update if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def draw_weighted_graph(graph):
    # Transforming the input to match expected format
    weighted_graph = {u: {v: {'weight': w} for v, w in edges.items()} for u, edges in graph.items()}
    G = nx.from_dict_of_dicts(weighted_graph)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=16, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'), font_color='red')
    
    plt.title("Graph Visualization")
    plt.show()

