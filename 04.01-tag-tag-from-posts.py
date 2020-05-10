# %% [markdown]
# # Creating a Tag Tag network
# %%
import pandas as pd
# import re
import itertools

# %%
fields = ['Id', 'PostTypeId', 'Tags']
df = pd.read_csv('data/gaming/csv/Posts.csv', usecols=fields)

# %%
print(df.head())
print(df.PostTypeId.value_counts())

# %%
dfQuestions = df[df.PostTypeId == 1][fields]

print(dfQuestions.PostTypeId.value_counts())
print(dfQuestions.head())

# %%
print('counts:\n', dfQuestions.count(), '\n')
print('missing values %:\n', dfQuestions.isna().sum() / (len(dfQuestions)) * 100)

# %% [markdown]
# # split the tags and start creating tag tag data set
#
# use a regular expression to capture vales  in sequence of <tag1>..<tagn>
# and return a list of tag values
#
# ```python
# import re
#
# str1 = '<distributions><normality-assumption>'
# pattern = '\<([^\>]*)\>'
# tags1  = re.findall(pattern=pattern, string=str1)
# ```

# %%

pattern = '\<([^\>]*)\>'

dfQuestions['TagsList'] = dfQuestions.Tags.str.findall(pat=pattern)

# ensuring tags list is sorted, important for creating edge combinations
dfQuestions.TagsList = dfQuestions['TagsList'].apply(lambda l: sorted(l))

dfQuestions['TagsCount'] = dfQuestions.TagsList.apply(len)
dfQuestions['EdgesCount'] = \
    (dfQuestions['TagsCount'] * (dfQuestions['TagsCount'] - 1) / 2).astype(int)

print(dfQuestions.TagsCount.value_counts())

# %%
# use itertools to generate all permutations of edges
# correct function to use is combinations

# %%
dfQuestions['edges'] = dfQuestions.TagsList.apply(
    lambda t: [e for e in itertools.combinations(t, 2)])

dfQuestions['edges_count'] = dfQuestions.edges.apply(len)
# %%
print(dfQuestions.head(10))

# %%
edges_exploded = dfQuestions[['Id', 'edges']][dfQuestions.edges_count > 0] \
    .explode('edges')
print(edges_exploded.head(10))

# %% [markdown]
# exploded list can now be used to create a network tags with edges where tags
# appeared in the same question
# we could  group by and count edge combinations to create weigted edges

# %%
edges_grouped = edges_exploded[['Id', 'edges']] \
    .groupby(['edges']) \
    .count() \
    .reset_index() \
    .rename(columns={'Id': 'weight'})

# %%
edges_grouped['v1'], edges_grouped['v2'] = zip(*edges_grouped['edges'])
print(edges_grouped.head())

# %%
filename = 'data/outputs/tags-tags.csv'
print(f'write tag-tag csv to file: {filename}')
edges_grouped[['v1', 'v2', 'weight']].to_csv(filename, index=False)
