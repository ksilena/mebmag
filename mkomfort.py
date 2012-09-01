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

url = "http://mkomfort.ru"
doc = soup(urlopen(url))
menu = select(doc, "div.menu")
span = select(menu[0],"span a")
soft = soup(urlopen(url + span[1]["href"]))

def clean_str(st):
    if st: st = kill_tag.sub('', str(st))
    if st: st = sub_quot.sub('"', st)
    if st: st = kill_space.sub(" ", st)
    if st: st = kill_str.sub('', st)
    return st.strip()
counter = 0
count = 0
p = select(soft, "div.name a")
href = soup(urlopen(url + p[0]["href"]))
for l in select(soft, "div.name a"):
    counter += 1
    href = soup(urlopen(url + l["href"]))
#d = soup(urlopen(url + p["href"]))
    h = select(href, "h1")
    size = select(href, "div.size")
    strong = select(href, "p")
    img = select(href, "a.highslide")
    print type(h[2])
    print "Название: ", h[2].string
    print  clean_str(size[0])
    print clean_str(strong[0])
    print url + img[0]["href"]
    print "-----------------------------------------------"
#print p[0]
#    if counter >0: break
#print href
counter = 0
for page in select(soft, "div.page a"):
    count += 1
    page_link = soup(urlopen(url + page["href"]))
    for i in select(page_link, "div.name a"):
        counter += 1
        href = soup(urlopen(url + i["href"])) 
        h = select(href, "h1")
        size = select(href, "div.size strong")
        strong = select(href, "p")
        img = select(href, "a.highslide")
        if len(strong) > 0:
            print h[2].string
            print clean_str(strong[0])
            print url + img[0]["href"]
#        if counter >0:break
#       print page_lin
#    if count >0:break


