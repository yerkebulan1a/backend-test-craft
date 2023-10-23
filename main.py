import xml.etree.ElementTree as ET
import pytest
# 1. Read element name and attributes
# 2. Compare attributes
# 3. print of number attributes, elements

AFATTRIBUTE = 'AFAttribute'
AFELEMENT = 'AFElement'

path_d = "WWD_AFD1.xml"
path_u = 'WWD_AFU1.xml'

tree_AFD = ET.parse(path_d)
tree_AFU = ET.parse(path_u)
root_d = tree_AFD.getroot()
root_u = tree_AFU.getroot()


def test_attribute():
    number_d = 0
    number_u = 0
    for element in root_d.iter(AFATTRIBUTE):
        number_d+=1
    for element in root_u.iter(AFATTRIBUTE):
        number_u+=1

    assert(number_d == number_u)

def test_element():
    number_d = 0
    number_u = 0
    for element in root_d.iter(AFELEMENT):
        number_d += 1
    for element in root_u.iter(AFELEMENT):
        number_u += 1

    assert (number_d == number_u)
