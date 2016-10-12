#! /usr/bin/python

import urllib2

url = 'http://m.weather.com.cn/data5/city.xml'
content = urllib2.urlopen(url).read()
#print content
provinces = content.split(',')
result = 'city = {\n'

url1 = 'http://m.weather.com.cn/data3/city%s.xml'
#for p in provinces[:8]:
for p in provinces:
    p_code = p.split('|')[0]
#    print p_code
    url2 = url1 % p_code
    content1 = urllib2.urlopen(url2).read()
    cities = content1.split(',')
#    print content1
    for c in cities[:3]:
        c_code = c.split('|')[0]
        url3 = url1 % c_code
        content2 = urllib2.urlopen(url3).read()
        districts = content2.split(',')
#        print content2
        for d in districts:
            d_pair = d.split('|')
            d_code = d_pair[0]
            name = d_pair[1]
#            print name
            url3 = url1 % d_code 
            content3 = urllib2.urlopen(url3).read()
#            print content3
            flag = content3.split('|')[0]
            if '<html>' in flag:
#                print code
                continue
   #         print type(code) 
            code = content3.split('|')[1]
            print code
            line = "  '%s': '%s',\n" %(name, code)
            result += line
#            print name + ':' + code
result += '}'
f = file('a.py','w')
f.write(result)
f.close()
