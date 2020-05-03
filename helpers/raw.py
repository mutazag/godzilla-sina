# import xml.etree.ElementTree as ET
# import xmltodict
# import json


def get_entity_keys(domain='gaming', entity='Badges', selected=True):
    """[summary]

    Keyword Arguments:
        domain {str} -- [description] (default: {'gaming'})
        entity {str} -- [description] (default: {'Badges'})

    Returns:
        [type] -- [description]
    """

    import pandas as pd

    entity_keys_csv_file = 'data\\{0}\\selected_keys\\{1}.csv' \
        if (selected is True) else 'data\\{0}\\keys\\{1}.csv'

    return list(pd.read_csv(
        entity_keys_csv_file.format(domain, entity),
        header=None, index_col=None)[0])


def get_entities_set(domain='gaming', selected=True):
    """[summary]

    Keyword Arguments:
        domain {str} -- [description] (default: {'gaming'})
    """

    entities = [
        'Badges', 'Comments', 'PostHistory', 'PostLinks', 'Posts',
        'Tags', 'Users', 'Votes']

    meta_path_template = 'raw\\{0}\\meta\\{1}.xml'
    path_template = 'raw\\{0}\\{1}.xml'
    csv_path_template = 'data\\{0}\\csv\\{1}.csv'
    tsv_path_template = 'data\\{0}\\tsv\\{1}.tsv'

    return_entities = [{
        'entity_name': entity,
        'entity_path': path_template.format(domain, entity),
        'entity_meta_path': meta_path_template.format(domain, entity),
        'entity_csv_path': csv_path_template.format(domain, entity),
        'entity_tsv_path': tsv_path_template.format(domain, entity),
        'entity_keys': get_entity_keys(domain, entity, selected)}
            for entity in entities
    ]
    return return_entities


def get_entities_dict(domain='gaming'):
    """[summary]

    Keyword Arguments:
        domain {str} -- [description] (default: {'gaming'})
    """

    entities = [
        'Badges', 'Comments', 'PostHistory', 'PostLinks', 'Posts',
        'Tags', 'Users', 'Votes']

    meta_path_template = 'raw\\{0}\\meta\\{1}.xml'
    path_template = 'raw\\{0}\\{1}.xml'
    csv_path_template = 'data\\{0}\\csv\\{1}.csv'
    tsv_path_template = 'data\\{0}\\tsv\\{1}.tsv'
    tsv_with_text_path_template = 'data\\{0}\\tsv\\{1}_text.tsv'

    return_entities = {entity: {
        'entity_name': entity,
        'entity_domain': domain,
        'entity_path': path_template.format(domain, entity),
        'entity_meta_path': meta_path_template.format(domain, entity),
        'entity_csv_path':
            csv_path_template.format(domain, entity),
        'entity_tsv_path':
            tsv_path_template.format(domain, entity),
        'entity_tsv_with_text_path':
            tsv_with_text_path_template.format(domain, entity),
        'entity_keys_with_text':
            get_entity_keys(domain, entity, selected=False),
        'entity_keys': get_entity_keys(domain, entity)} for entity in entities
    }
    return return_entities


def parse_one_node(node, attrib_keys):
    """[summary]

    Arguments:
        node {[type]} -- [description]
        attrib_keys {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    import urllib
    rich_text_fields = {'Body', 'Title', 'AboutMe', 'Text', 'Comment'}
    node_attribs_dict = {}
    for k, key in enumerate(attrib_keys):
        # node_attribs_dict[key] = node.attrib[key]
        value = node.get(key)
        if (key in rich_text_fields) and (value is not None):
            value = urllib.parse.quote(value)

        node_attribs_dict[key] = value
    return node_attribs_dict


def parse_root(root, attribs):
    """[summary]

    Arguments:
        root {[type]} -- [description]
        attribs {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    rows = []
    for i, node in enumerate(root):
        node_attribs_dict = parse_one_node(node, attribs)
        rows.append(node_attribs_dict)
    print(f'process {i} items')
    print(len(rows))
    return rows


def convert_xml_to_csv(entity_dict, keeptext=False):
    import csv
    # {'entity_name': 'Posts',
    # 'entity_domain': 'gaming',
    # 'entity_path': 'raw\\gaming\\Posts.xml',
    # 'entity_meta_path': 'raw\\gaming\\meta\\Posts.xml',
    # 'entity_csv_path': 'data\\gaming\\Posts.csv',
    # 'entity_keys': ['Score',...]}

    import xml.etree.ElementTree as ET
    tree = ET.parse(entity_dict['entity_path'])
    root = tree.getroot()
    nodes_list = parse_root(
        root,
        entity_dict['entity_keys_with_text']
        if keeptext is True else
        entity_dict['entity_keys'])

    import pandas as pd
    df = pd.DataFrame(nodes_list)
    if keeptext is True:
        df.to_csv(
            entity_dict['entity_tsv_with_text_path'],
            index=False,
            quoting=csv.QUOTE_NONE,
            quotechar="",
            escapechar="\\",
            sep='\t')
    else:
        df.to_csv(
            entity_dict['entity_csv_path'],
            index=False)
    return df.count()


if __name__ == '__main__':
    print('helpers.raw module')
