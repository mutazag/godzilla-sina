# import xml.etree.ElementTree as ET
# import xmltodict
# import json


def get_entity_keys(domain='gaming', entity='Badges'):
    """[summary]

    Keyword Arguments:
        domain {str} -- [description] (default: {'gaming'})
        entity {str} -- [description] (default: {'Badges'})

    Returns:
        [type] -- [description]
    """

    import pandas as pd
    entity_keys_csv_file = 'data\\{0}\\keys\\{1}.csv'

    return list(pd.read_csv(
        entity_keys_csv_file.format(domain, entity),
        header=None, index_col=None)[0])


def get_entities_set(domain='gaming'):
    """[summary]

    Keyword Arguments:
        domain {str} -- [description] (default: {'gaming'})
    """

    entities = [
        'Badges', 'Comments', 'PostHistory', 'PostLinks', 'Posts',
        'Tags', 'Users', 'Votes']

    meta_path_template = 'raw\\{0}\\meta\\{1}.xml'
    path_template = 'raw\\{0}\\{1}.xml'
    csv_path_template = 'data\\{0}\\{1}.csv'

    return_entities = [{
        'entity_name': entity,
        'entity_path': path_template.format(domain, entity),
        'entity_meta_path': meta_path_template.format(domain, entity),
        'entity_csv_path': csv_path_template.format(domain, entity),
        'entity_keys': get_entity_keys(domain, entity)} for entity in entities
    ]
    return return_entities


def parse_one_node(node, attrib_keys):
    """[summary]

    Arguments:
        node {[type]} -- [description]
        attrib_keys {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    node_attribs_dict = {}
    for k, key in enumerate(attrib_keys):
        # node_attribs_dict[key] = node.attrib[key]
        node_attribs_dict[key] = node.get(key)
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


if __name__ == '__main__':
    print('helpers.raw module')
