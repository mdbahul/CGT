import networkx as nx
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

# Example degree sequence
degree_sequence = [3, 3, 2, 2, 2, 2]  # Example valid degree sequence

# Create the graph
graph = create_graph_from_deg_sequence(degree_sequence)

# Plot the graph if it's valid
if graph:
    plot_graph(graph)
    
