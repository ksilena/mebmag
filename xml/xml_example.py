#!/usr/bin/python
#-*- coding: utf-8 -*-
from lxml import etree
xml=etree.parse('/home/zol/src/export201208261142.xml')
root=xml.getroot()
def printElement(a,b="    "):
    if len(a) > 0:
        print b, a.tag,  a.text
        for ij in a:
            printElement(ij,b+"    ")
    else:
        print "     ", a.tag,  a.text
#handle = etree.tostring(root, pretty_print=True, encoding='utf-8')
#with open("new.xml", "w") as f:
#    f.write(handle)
print len(root[1]), type(root[1])
for i in root[1][15][1]:
    printElement(i)
