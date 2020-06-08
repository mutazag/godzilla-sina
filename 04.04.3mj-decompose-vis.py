# %% 
import networkx as nx
# from networkx.algorithms import centrality
from networkx.readwrite import gexf
import pandas as pd
import matplotlib.pyplot as plt
from networkx.drawing import layout
## https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.drawing.nx_agraph.graphviz_layout.html 

# %%
print('start')
G = gexf.read_gexf('3mj/subgraph--1-start.gexf')
print('generate layout')
sp = layout.kamada_kawai_layout(G)

degrees = pd.DataFrame(dict(G.degree).items(), columns=['tag', 'degree'])

print(nx.__version__)
print('before')
print(nx.info(G))

nodes_zero_degree = (degrees.query('degree == 0')['tag'].to_list())
G.remove_nodes_from(nodes_zero_degree)

print('after')
print(nx.info(G))

# %% 
df_decompose = pd.read_csv('3mj/decomposed_3mj.csv')[['iteration', 'tag','filename']]
# %%


def plot_decompose(r): 
    
    ego_node = df_decompose.query(f'iteration == {r.iteration+1}')['tag'].iloc[0]
    print(r.iteration, ego_node, sp[ego_node])
    g_node = gexf.read_gexf(r.filename)
    # sp1 = layout.kamada_kawai_layout(g_node)
    nx.draw(g_node, pos=sp, node_color='#0C84B6', node_size=5, with_labels=False )
    # nx.draw_networkx_nodes(g_node, pos=sp, nodelist=[ego_node], node_size=10, node_color='#0E59A2')
    nx.draw_networkx_edges(g_node, pos=sp, alpha=0.04, edge_color='#D8E7F5')


    plt.axis('off')
    plt.savefig('images/'+r.filename.replace('.gexf','.png'), dpi=500)


df_decompose.iloc[[1,200],:].apply(plot_decompose, axis=1)
# for r in df_decompose.iloc[0,:]: 
#     print(type(r.iteration))

    # ego_node = 'technical-issues'
    # nx.draw(G, pos=sp, node_color='#0C84B6', node_size=10, with_labels=False, edge_color='#D8E7F5')
    # # Draw ego as large and red
    # nx.draw_networkx_nodes(G, pos=sp, nodelist=[ego_node], node_size=30, node_color='#0E59A2')
    # plt.axis('off')
    # plt.savefig('images/test.png', dpi=500)

# %%
df_decompose.apply(plot_decompose, axis=1)

# %%
