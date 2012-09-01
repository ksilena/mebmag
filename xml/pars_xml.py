#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.dom.minidom import *
dom = xml.dom.minidom.parse("/home/zol/src/export201208261142.xml")
dom.normalize()
def output_tree(node, level=0):
   if node.nodeType == node.TEXT_NODE:
     if node.nodeValue.strip():
       print ". "*level, node.nodeValue.strip()
   else:   # ELEMENT_NODE или DOCUMENT_NODE
     atts = node.attributes or {}
     att_string = ", ".join(
         ["%s=%s " % (k, v)  for k, v in atts.items()])
     print ". "*level, node.nodeName, att_string
     for child in node.childNodes:
       output_tree(child, level+1)
name =  dom.getElementsByTagName(u'Свойство')
print name.tagName
