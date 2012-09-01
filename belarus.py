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
url = "http://mebelbelarusi.ru"
doc = soup(urlopen(url))
counter = 0
c_2 = 0
div_block = select(doc, "ul.left_menu a")
for a in select(doc, "ul.left_menu a"):
    counter += 1
    li = soup(urlopen(url + a["href"]))
    name =  select(li, "a.p_name")
    if name:
        for b in name:
            i_name = soup(urlopen(url + b["href"]))
            img = select(i_name, "a#link")
            mat = select(i_name, "ul.item_par")
            h3 = select(i_name, "h3")
            print "Название:", clean_str(h3[0])
            print clean_str(mat[0])
            print img
