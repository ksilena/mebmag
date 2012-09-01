#!/usr/bin/python
from BeautifulSoup import BeautifulSoup as soup
from soupselect import select
from urllib2 import urlopen
import re
url="http://www.mebel-art.net"
doc=soup(urlopen(url))
#div = select(doc, "div#main_menu_block")
#menu = select(, "div.catalog-sension-list")
#url_left_0 = select(doc, "a.left_menu_0")
#url2 = soup(urlopen(url + url_left_0[0]["href"]))
#tag = doc.findALL('a')

print doc

