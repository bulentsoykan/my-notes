import matplotlib.pyplot as plt
import networkx as nx
from mpl_toolkits.mplot3d import Axes3D

# Initialize 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Define layers (Graphs)
layers = {
    "Layer1": nx.gnp_random_graph(10, 0.4),
    "Layer2": nx.gnp_random_graph(10, 0.4),
}

# Define Z positions for each layer
layer_z_positions = {"Layer1": 0, "Layer2": 1}  # Adjust the spacing as necessary

# Plot each layer
for layer_name, graph in layers.items():
    z_pos = layer_z_positions[layer_name]
    for edge in graph.edges():
        x, y = zip(*[graph.nodes[node]["pos"] for node in edge])
        z = [z_pos, z_pos]
        ax.plot(x, y, z, color="blue")

    for node in graph.nodes():
        x, y = graph.nodes[node]["pos"]
        ax.scatter(x, y, z_pos, color="red")

# Set labels and title
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis (Layers)")
plt.title("3D Visualization of Multi-Layer Hypergraphs")

plt.show()
