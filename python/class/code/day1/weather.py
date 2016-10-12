#! /usr/bin/python
##-*- coding: utf-8 -*-

import urllib2
import json
from city import city
cityname = raw_input('city name ?\n')
citycode = city.get(cityname)
if citycode:
    try:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
        content = urllib2.urlopen(url).read()
        #print content
        data = json.loads(content)
        result = data['weatherinfo']
        str_temp = ('%s: %s ~ %s') % (result['weather'],result['temp1'],result['temp2'])
        
        print str_temp
    except:
        print 'failed'
else:
    print 'no city'
#print type(content)
#print type(data)
