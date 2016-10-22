#! /usr/bin/python

results = []

f = file('scores')
lines = f.readlines()
#print lines
f.close()

for line in lines:
#    print line
    data = line.split()
#    print data

    sum = 0 
    for score in data[1:]:
        sum += int(score)
    result = '%s\t-> %d\n' % (data[0],sum)
#        print result
    results.append(result)
            
out = file('result.txt','w')
out.writelines(results)
out.close()
