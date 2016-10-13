#! /usr/bin/python

import re
#text = 'Hi,I am shirley Hilton, I am his wife'
text = 'site sea sue sweet see case sse ssee loses'
m = re.findall(r"\bs\S*?e\b",text)
m = re.findall(r"\bs.*?e\b",text)
#m = re.findall(r"[Hh]i*",text)
#m = re.findall(r"\bi\b",text)

if m:
    print m
else:
    print 'not match'
