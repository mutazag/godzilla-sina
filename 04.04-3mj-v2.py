# %%
import networkx as nx
from networkx.algorithms import centrality
from networkx.algorithms import components
from networkx.readwrite import gexf
import pandas as pd
import tqdm
# import matplotlib.pyplot as plt
# import scipy


# %%
G = gexf.read_gexf('data/outputs/tags-tags.gexf')
print(nx.__version__)
print(nx.info(G))

# %%


def df_from_betweeness(inG):
    print(f'calculate betweenness, network of size {inG.order()}')
    temp_betweenness = centrality.betweenness_centrality(inG)
    return pd.DataFrame(
        temp_betweenness.items(),
        columns=['tag', 'betweenness']).sort_values('betweenness', ascending=False)

# %%
# calc betweenness for the first time and subgraph to remove nodes that have 0 betweeness


df_betweenness = df_from_betweeness(G)
df_betweenness_gt_0 = df_betweenness[df_betweenness.betweenness > 0].sort_values('betweenness', ascending=False)

# The result subgraph of only nodes of betweeenness > 0
G_betweenness_gt_0 = nx.subgraph(G, df_betweenness_gt_0.tag)


#  %%

def make_row(i, tag, betweenness, inG):
    filename = '3mj/subgraph-{0}.gexf'
    return {
        'iteration': i,
        'tag': tag,
        'betweeness': betweenness,
        'nodes': inG.order(),
        'edges': inG.size(),
        'average_degree': inG.size() / inG.order(),
        'no_connected_components': components.number_connected_components(inG),
        'filename': filename.format(f'{i:02d}-{tag}')
    }
# %%
G_start = G_betweenness_gt_0.copy() 



df_decompose_g = pd.DataFrame({
    # 'iteration': [],|
    # 'tag': [], 
    # 'betweeness': [], 
    # 'nodes': [], 
    # 'edges': [], 
    # 'filename': [] 
    })

df_decompose_g = df_decompose_g.append(make_row(-1, 'start', 0, G_start), ignore_index=True)

gexf.write_gexf(G_start, df_decompose_g.iloc[0, :]['filename'])
# %%

k = 500
for i in tqdm.tqdm(range(k)):
    temp_betweenness_df = df_from_betweeness(G_start)
    tag_str, betweenness_value = temp_betweenness_df.iloc[0, :].tag, temp_betweenness_df.iloc[0, :].betweenness
    df_decompose_g = df_decompose_g.append(make_row(i, tag_str, betweenness_value, G_start), ignore_index=True)
    print(f"{i:02d}-{tag_str}: {betweenness_value} >>>> {df_decompose_g.iloc[i+1, :]['filename']}")
    G_start.remove_node(tag_str)
    # print(df_decompose_g.iloc[i+1,:]['filename'])
    gexf.write_gexf(G_start, df_decompose_g.iloc[i+1,:]['filename'])

df_decompose_g.to_csv('3mj/decomposed_3mj.csv')
# %%
df_decompose_g.edges.plot.line()


# %%
df_decompose_g.no_connected_components.plot.line()

# %%
