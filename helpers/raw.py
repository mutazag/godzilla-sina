import xml.etree.ElementTree as ET
import xmltodict
import json

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
        #node_attribs_dict[key] = node.attrib[key]
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