#!/usr/bin/python
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup as soup
from soupselect import select
from urllib2 import urlopen
import re

################ regular expression ####################
kill_tag = re.compile('<[^<]*>') #поиск тэга
sub_quot = re.compile('&laquo; *| *&raquo;|&quot;') #поиск кавычек
kill_space = re.compile('&nbsp;| +|\t+') #поиск пробел и табуляции
kill_str = re.compile('\n|\r') #поиск конца строки
###########################################################

##################### function for cleaning str ############
def clean_str(st):
    if st: st = kill_tag.sub('', str(st))
    if st: st = sub_quot.sub('"', st)
    if st: st = kill_space.sub(" ", st)
    if st: st = kill_str.sub('', st)
    return st.strip()
#############################################################

# set initial variables #
url = "http://mebelbelarusi.ru"
doc = soup(urlopen(url))
counter = 0
c_2 = 0
div_block = select(doc, "ul.left_menu a")
# parse menu links #
for a in div_block:
    counter += 1
    li = soup(urlopen(url + a["href"]))
    attr = select(li, "span.f_right a")
    if len(attr)>0:
            krovat = soup(urlopen(url + attr[0]["href"]))
            name = select(krovat, "a.p_name")
            for i in name:
                    i_name = soup(urlopen(url + i["href"]))
                    h3 = select(i_name, "h3")
                    img = select(i_name, "a#link")
                    mat = select(i_name, "ul.item_par")
                    print "Название:", clean_str(h3[0])
                    print clean_str(mat[0])
                    if img:
                        print url + img[0]["href"]
                    print "=================================================="

         
