import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(
    os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


def test_make_one_point():
    pass


def test_parse_on_node():
    attrib_keys = ['Id', 'UserId']
    ret_result = {'Id': '1', 'UserId': '2'}
    xml = '<badges><row Id="1" UserId="2" Name="Autobiographer" '\
        'Date="2010-07-07T19:08:45.757" Class="3" TagBased="False" /></badges>'
    from xml.etree import ElementTree as et
    root = et.fromstring(xml)

    from helpers import raw
    node_attribs_dict = raw.parse_one_node(root[0], attrib_keys)

    if node_attribs_dict == ret_result:
        pass


def test_parse_root():
    attrib_keys = ['Id', 'UserId']
    xml = '<badges>'\
        '<row Id="1" UserId="2" Name="Autobiographer" '\
        'Date="2010-07-07T19:08:45.757" Class="3" TagBased="False" />'\
        '<row Id="2" UserId="4" Name="User2" '\
        'Date="2010-07-08T20:00:15.000" Class="4" TagBased="True" />'\
        '</badges>'
    ret_result = [{'Id': '1', 'UserId': '2'}, {'Id': '2', 'UserId': '4'}]

    from xml.etree import ElementTree as et
    root = et.fromstring(xml)

    from helpers import raw
    ret = raw.parse_root(root, attrib_keys)

    print(ret)

    if ret == ret_result:
        pass


def test_dummy_fail():
    assert False


if __name__ == '__main__':
    test_parse_on_node()
    test_parse_root()
