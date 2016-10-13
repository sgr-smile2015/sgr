#! /usr/bin/python

import re
#text = 'Hi,I am shirley Hilton, I am his wife'
#text = 'site sea sue sweet see case sse ssee loses'
text = '13924102341 23456789 15807711a22 12113421 12345678900'
#m = re.findall(r"\bs\S*?e\b",text)
m = re.findall(r"1\d{10}",text)
#m = re.findall(r"[Hh]i*",text)
#m = re.findall(r"\bi\b",text)
#m = re.findall(r"\b.*\S\b",text)

if m:
    print m
else:
    print 'not match'
