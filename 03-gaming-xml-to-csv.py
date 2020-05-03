# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from helpers import *


# %%
domain = 'gaming'

domain_entities = raw.get_entities_dict(domain=domain)


# %%
domain_entities['Posts']

# %% [markdown]
# # Process Badges

# %%
ret = raw.convert_xml_to_csv(domain_entities['Badges'], keeptext=False)


# %%
ret


# %%
ret = raw.convert_xml_to_csv(domain_entities['Badges'], keeptext=True)


# %%
ret

# %% [markdown]
# # Process Comments

# %%
ret = raw.convert_xml_to_csv(domain_entities['Comments'], keeptext=False)


# %%
ret


# %%
ret = raw.convert_xml_to_csv(domain_entities['Comments'], keeptext=True)


# %%
ret

# %% [markdown]
# # Process Post History

# %%
ret = raw.convert_xml_to_csv(domain_entities['PostHistory'], keeptext=False)


# %%
ret


# %%
ret = raw.convert_xml_to_csv(domain_entities['PostHistory'], keeptext=True)


# %%
ret

# %% [markdown]
# # Process Links

# %%
ret = raw.convert_xml_to_csv(domain_entities['PostLinks'], keeptext=False)


# %%
ret


# %%
ret = raw.convert_xml_to_csv(domain_entities['PostLinks'], keeptext=True)


# %%
ret

# %% [markdown]
# # Process Posts

# %%
ret = raw.convert_xml_to_csv(domain_entities['Posts'], keeptext=False)


# %%
ret


# %%
ret = raw.convert_xml_to_csv(domain_entities['Posts'], keeptext=True)


# %%
ret

# %% [markdown]
# # Process Tags

# %%
ret = raw.convert_xml_to_csv(domain_entities['Tags'], keeptext=False)


# %%
ret


# %%
ret = raw.convert_xml_to_csv(domain_entities['Tags'], keeptext=True)


# %%
ret

# %% [markdown]
# # Process Users

# %%
ret = raw.convert_xml_to_csv(domain_entities['Users'], keeptext=False)


# %%
ret


# %%
ret = raw.convert_xml_to_csv(domain_entities['Users'], keeptext=True)


# %%
ret

# %% [markdown]
# # Process Votes

# %%
ret = raw.convert_xml_to_csv(domain_entities['Votes'], keeptext=False)


# %%
ret


# %%
ret = raw.convert_xml_to_csv(domain_entities['Votes'], keeptext=True)


# %%


