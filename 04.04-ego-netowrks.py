import networkx as nx
from networkx.algorithms import centrality
from networkx.readwrite import gexf
import pandas as pd
import matplotlib.pyplot as plt

G = gexf.read_gexf('data/outputs/tags-tags.gexf')
print(nx.__version__)
print(nx.info(G))

ego_node = 'minecraft-java-edition'
radius = 2

G_ego = nx.ego_graph(G, ego_node, radius=radius)
print(nx.info(G_ego))

sp = nx.spring_layout(G_ego)

plt.axis('off')


nx.draw(G_ego, pos=sp, node_color='#0E59A2', node_size=50, with_labels=False, edge_color='#D8E7F5')
# Draw ego as large and red
nx.draw_networkx_nodes(G_ego, pos=sp, nodelist=[ego_node], node_size=300, node_color='#0C84B6')

plt.show()