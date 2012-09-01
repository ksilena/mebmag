#!/usr/bin/python
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup as soup
from soupselect import select
from urllib2 import urlopen
import re
    
kill_tag = re.compile('<[^<]*>')
sub_quot = re.compile('&laquo; *| *&raquo;|&quot;')
kill_space = re.compile('&nbsp;| +|\t+') 
kill_str = re.compile('\n|\r')

def clean_str(st):
    if st: st = kill_tag.sub('', str(st))
    if st: st = sub_quot.sub('"', st)
    if st: st = kill_space.sub(" ", st)
    if st: st = kill_str.sub('', st)
    return st.strip()

url="http://bravomebel.ru"
doc=soup(urlopen(url))
url_left_0 = select(doc, "a.left_menu_0")
url2 = soup(urlopen(url + url_left_0[0]["href"]))
url_left_1 = select(url2, "a.left_menu_1")
url3 = soup(urlopen(url + url_left_1[0]["href"]))
counter = 0
catalog = select(url3, "a.catalog_folder b")
for l in  select(url3, "a.catalog_folder b"):
    counter += 1
    p  = soup(urlopen(url + l.parent["href"]))
    h = select(p, "h1")[0]
    tbody = select(h.parent.parent.parent, "tbody tr")[1]
    q  = h.parent.parent.parent.findAll("img")
#    img = select(q, "img")
    c = 0
    for hh in q:
       c+=1

#       print "==========================" + str(c) + "================"
       print hh["src"]
    print l.parent["href"]
    print clean_str(h)
    print "Описание: ", clean_str(tbody)
    print clean_str(select(h.parent.parent.parent, "tbody tr")[2])
    table = select(h.parent.parent.parent, "tbody tr")[3]
    tr = select(table, "tr")
    s = kill_tag.sub('', str(tr))
    print "----------------------------"
    for i in tr:
       print "|" + clean_str(select(i, "td")[0]) + "|" + clean_str(select(i, "td")[1]) + "|"
       print "----------------------------"
    if counter >0:break
#        print "Описание: " + str(st)
#    if counter > 0:break



