import networkx as nx
import jhola as jhol
import matplotlib.pyplot as plt

#processes havel_hakimi algorithms
def havel_hakimi(seq):
    # if seq is empty or only contains zeros,
    # degree sequence is valid
    if len(seq) < 1 or all(deg == 0 for deg in seq):
        print("Finished! Graph IS constructable with Havel Hakimi algorithm.")
        return True

    print(seq, end="")
    seq.sort(reverse=True)  # Sort in non-increasing (descending) order
    print(" --sort--> ", end="")
    print(seq)

    first = seq[0]  # The largest element now becomes the first one
    if first > len(seq) - 1:
        print("Failed! Graph IS NOT constructable with Havel Hakimi algorithm.")
        return False

    print(seq, end="")

    # remove the largest element (which is now at index 0)
    seq.pop(0)

    # iterate seq forwards and reduce elements
    for num in range(first):
        if seq[num] > 0:
            seq[num] -= 1
        else:
            print("\nFailed! Graph is not constructable with Havel Hakimi algorithm")
            return False

    print(" --alg-->", end="")
    print(seq)

    # recursive call
    return havel_hakimi(seq)

def is_valid_deg_sequence(deg_seq):
    # Check if the degree sequence is valid using the Erdős-Gallai theorem
    return havel_hakimi(deg_seq.copy())

def create_graph_from_deg_sequence(deg_seq):
    # Check if the degree sequence is valid
    if not is_valid_deg_sequence(deg_seq):
        return None
    
    # Create the graph using the Havel-Hakimi algorithm
    G = nx.havel_hakimi_graph(deg_seq)
        
    return G

def plot_graph(G):
    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black')
    plt.show()

# Check if the graph is connected
def is_connected(graph):
    start_node = next((node for node in graph if len(graph[node]) > 0), None)
    if start_node is None:
        return True  # Trivially connected if no edges

    visited = set()

    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start_node)

    for node in graph:
        if len(graph[node]) > 0 and node not in visited:
            return False

    return True

# Check if the graph is Eulerian
def is_eulerian(graph):
    odd_degree_nodes = [node for node in graph if len(graph[node]) % 2 != 0]

    if not is_connected(graph):
        print("The graph is not connected, so it cannot be Eulerian.")
        return False
    
    if len(odd_degree_nodes) == 0:
        print("The graph has an Eulerian circuit.")
        return True
    elif len(odd_degree_nodes) == 2:
        print(f"The graph has an Eulerian path. The odd degree vertices are: {odd_degree_nodes}")
        return True
    else:
        print(f"The graph is not Eulerian. The vertices with odd degrees are: {odd_degree_nodes}")
        return False

# Example degree sequence
degree_sequence = [ 4, 2, 2, 2,2]  # Example valid degree sequence

# Create the graph
graph = create_graph_from_deg_sequence(degree_sequence)

# Plot the graph if it's valid
if graph:
    plot_graph(graph)
    is_eulerian(graph)

graph_dict = jhol.deg_seq_to_dict(degree_sequence)
print("Euler Path : ", jhol.find_eulerian_path(graph_dict))
    