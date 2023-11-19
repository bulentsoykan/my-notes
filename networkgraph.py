import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes and edges for each layer
# For simplicity, this example uses two layers with some inter-layer edges
G.add_edges_from([(1, 2), (2, 3)])  # Layer 1 edges
G.add_edges_from([(4, 5), (5, 6)])  # Layer 2 edges
G.add_edges_from([(3, 4)])          # Inter-layer edge

# Position nodes for visualization
pos = {1: (0, 1), 2: (1, 1), 3: (2, 1),  # Layer 1 positions
       4: (0, 0), 5: (1, 0), 6: (2, 0)}  # Layer 2 positions

# Draw the graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')

# Show plot
plt.show()
