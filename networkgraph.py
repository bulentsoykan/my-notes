import matplotlib.pyplot as plt
import networkx as nx
from mpl_toolkits.mplot3d import Axes3D

# Initialize 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Example: Creating two layers of graphs
G1 = nx.Graph()
G1.add_edges_from([(1, 2), (2, 3)])  # Layer 1 edges

G2 = nx.Graph()
G2.add_edges_from([(4, 5), (5, 6)])  # Layer 2 edges

# Define positions for each node in 3D space
positions = {
    1: (0, 1, 1),
    2: (1, 1, 1),
    3: (2, 1, 1),
    4: (0, 0, 0),
    5: (1, 0, 0),
    6: (2, 0, 0),
}

# Draw the nodes
for node, pos in positions.items():
    ax.scatter(*pos, s=100)  # Adjust size as needed

# Draw the edges
for edge in G1.edges:
    xs, ys, zs = zip(*[positions[v] for v in edge])
    ax.plot(xs, ys, zs, color="blue")

for edge in G2.edges:
    xs, ys, zs = zip(*[positions[v] for v in edge])
    ax.plot(xs, ys, zs, color="red")

# Customize the plot
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Layer (Z Axis)")

plt.show()
