from xml.etree import ElementTree
dic = {'red': 0, 'green': 0, 'blue': 0}
root = ElementTree.fromstring(input())
roots = [root.attrib, 1]
kids = []
for elm in root.findall('cube'):
    kids.append([elm.attrib, 2])
    for chl in elm:
        kids.append([chl.attrib, 3])
dic[list(root.attrib.values())[0]] += 1
for ls in kids:
    dic[ls[0]['color']] += ls[-1]
print(*dic.values())
