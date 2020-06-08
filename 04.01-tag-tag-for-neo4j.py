# %% [markdown]
# # Neo4j tags and edges. 
#  create import files for tags network and the post -Tagged With-> tag edges file
# 
# Tags.csv header: :ID, :LABEL --> values (tagname, Tag)
# rel_posts_tag.csv header: :START_ID,:END_ID,:TYPE --> values (postid, tagname, TAGGED_WITH)
# %%
import pandas as pd
# import re
import itertools
import os
# %%
fields = ['Id', 'PostTypeId', 'Tags']
df = pd.read_csv('data/gaming/csv/Posts.csv', usecols=fields)

# %% [markdown]
# anything that does not have a tag is not a question,
# printing `PostTypId` for posts that dont have tags, 
# and they are all quetsions, type 1
print(df[~df.Tags.isna()].PostTypeId.value_counts())

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

# %%
# ensuring tags list is sorted, important for creating edge combinations
dfQuestions.TagsList = dfQuestions['TagsList'].apply(lambda l: sorted(l))

# %% 
dfPost_Tags = dfQuestions[['Id', 'TagsList']].explode('TagsList') \
    .rename(columns={'TagsList': 'Tag'})
dfPost_Tags['TagId'] = 'tag.' + dfPost_Tags['Tag'] 
# %% [markdown]
# everything i need is now in dfPost_Tags
# create thenodes csv and rel csv from this df 

# %% 
# nodes csv, header: :ID,:LABEL

dfTags = dfPost_Tags[['Tag', 'TagId']] \
    .groupby(['Tag', 'TagId']) \
    .first().reset_index() \
    .rename(columns={'TagId': ':ID'})
dfTags[':LABEL'] = 'Tag'

dfTags = dfTags[[':ID', 'Tag', ':LABEL']]


# rel csv, header: :START_ID, :END_ID, :TYPE
#   :START_ID - post ID
#   :END_ID - Tag
#   :TYPE - TAGGED_WITH
dfPostsTags = dfPost_Tags \
    .rename(columns= {'Id': ':START_ID', 'TagId': ':END_ID'})
dfPostsTags[':TYPE'] = 'TAGGED_WITH'
dfPostsTags = dfPostsTags[[':START_ID', ':END_ID', ':TYPE']]


# %% 
# save to file 

neo4jroot = 'data/gaming/neo4j/'

dfTags.to_csv(os.path.join(neo4jroot,'Tags.csv'), index=False)
dfPostsTags.to_csv(os.path.join(neo4jroot,'rel_posts_tags.csv'), index=False)

# %%
