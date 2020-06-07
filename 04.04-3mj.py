# %% 
import networkx as nx
from networkx.algorithms import centrality
from networkx.algorithms import components
from networkx.readwrite import gexf
import pandas as pd
import matplotlib.pyplot as plt
import scipy


# %%
G = gexf.read_gexf('data/outputs/tags-tags.gexf')
print(nx.__version__)
print(nx.info(G))

# %%
g_betweenness = centrality.betweenness_centrality(G)
# %%
df_betweenness = pd.DataFrame(g_betweenness.items(), columns=['tag','betweenness']).sort_values('betweenness',ascending=False)
df_betweenness_gt_0 = df_betweenness[df_betweenness.betweenness > 0].sort_values('betweenness',ascending=False)

G_betweenness_gt_0 = nx.subgraph(G, df_betweenness_gt_0.tag)

# %%
#labels = {c: f'${c}$' for i, c in enumerate(G.nodes())}

# %%
pos = nx.spring_layout(G)

# %% 
pos_gt_0 = nx.spring_layout(G_betweenness_gt_0)

# %%
nx.draw_networkx_nodes(G_betweenness_gt_0, pos=pos_gt_0, node_color='grey', node_size=500, alpha=0.8)
# nx.draw_networkx_labels(G, pos=pos, labels=labels, font_size=16)
nx.draw_networkx_edges(G_betweenness_gt_0, pos=pos_gt_0, width=1.5, alpha=0.5, edge_color='g')

#  %% 

def make_row(i, tag, betweenness, inG):
    filename = '3mj/subgraph-{0}.gexf'
    return {
    'iteration': i,
    'tag': tag, 
    'betweeness': betweenness, 
    'nodes': inG.order(),
    'edges':  inG.size(), 
    'no_connected_components': components.number_connected_components(inG), 
    'filename': filename.format(f'{i:02d}-{tag}') 
    }
# %%
k = 500
G_start = G_betweenness_gt_0.copy() 



df_decompose_g = pd.DataFrame({
    'iteration': [],
    'tag': [], 
    'betweeness': [], 
    'nodes': [], 
    'edges': [], 
    'filename': [] 
    })

df_decompose_g = df_decompose_g.append(make_row(-1,'start',0,G_start), ignore_index=True)

gexf.write_gexf(G_start, filename.format('start'))
for i in range(k): 
    node_str = df_betweenness_gt_0.iloc[i,:].tag
    f = filename.format(f'{i:02d}-{node_str}')
    print(f"{i:02d}-{node_str}: {df_betweenness_gt_0.iloc[i,:].betweenness} >>>> {f}")
    G_start.remove_node(node_str)
    df_decompose_g = df_decompose_g.append(make_row(i,node_str,df_betweenness_gt_0.iloc[i,:].betweenness,G_start),ignore_index=True)
    # print(df_decompose_g.iloc[i+1,:]['filename'])
    # gexf.write_gexf(G_start,df_decompose_g.iloc[i+1,:]['filename'])
# %%
df_decompose_g.edges.plot.line()

# %%
df_decompose_g.no_connected_components.plot.line()

# %%
