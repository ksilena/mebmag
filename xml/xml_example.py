#!/usr/bin/python
#-*- coding: utf-8 -*-
from lxml import etree
xml=etree.parse('/home/zol/src/export201208261142.xml')
root=xml.getroot()
#handle = etree.tostring(root, pretty_print=True, encoding='utf-8')
#with open("new.xml", "w") as f:
#    f.write(handle)
print len(root), type(root)
for i in root[1][15][1]:
    print i.tag,  i.text
