#!/bin/bash
geom=`identify $1 |awk '{print $3}'`
convert -gravity NorthEast -extent $geom  logo.jpg  $1 -compose Divide -composite   dst.jpg
convert dst.jpg \( -gravity NorthEast -extent $geom -background black ../mask.gif -negate \) -alpha off -compose CopyOpacity -composite \( +clone -channel RGBA -blur 0x2 +channel -alpha off \) +swap -compose Over -composite dst.jpg
mogrify   -region 370x77+599+3 -median 2 dst.jpg
