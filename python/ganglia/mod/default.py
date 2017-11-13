#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import time

next_pos = 0
descriptors = list()


def file_to_dic(source):
    ret = list()
    with open(source) as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            print '-->%s' % line
            l = line.split(':')
            ret.extend(l)
            #ret.append(l)
    return dict(zip(ret[0::2], ret[1::2]))

#conf = {
#        'test': '/mnt/log/test',
#        'data': '/mnt/data/data',
#}

conf = file_to_dic('config')

log_seek = {}
for e in conf:
    log_seek[e] = 0


def find_error(name, app, path):
    global next_pos
    #print '-->%s' % path
    count = 0
    target_file = open(path, 'rb')
    error = 'ERROR'
    target_file.seek(log_seek[app], 0)
    while True:
        start = target_file.read(8192*1024)
        if not start:
            break
        count += start.count(error)
        log_seek[app] = target_file.tell()
    target_file.close()
    #print('error count is:', count)
    #print log_seek
    return int(count)


def metric_init(params):
    global descriptors
    #print params
    desc_skel = {
        'name': 'xxx',
        'call_back': 'xxx',
        'time_max': 90,
        'value_type': 'uint',
        'units': 'Num',
        'slope': 'both',
        'format': '%u',
        'description': 'xxx',
        'groups': 'app log'
    }
    for app, path in conf.iteritems():
        descriptors.append(create_desc(desc_skel, {'name': 'log_'+app,
                                                   'call_back': lambda name, app=app, path=path: find_error(name, app, path),
                                                   'description': 'Find error in '+app}))
    return descriptors


def metric_cleanup():
    pass


def create_desc(skel, prop):
    d = skel.copy()
    for k, v in prop.iteritems():
        d[k] = v
    return d


#This code is for debugging and unit testing
if __name__ == '__main__':
    metric_init({})
    while True:
        for d in descriptors:
            v = d['call_back'](d['name'])
            print ('value for %s is '+d['format']) % (d['name'], v)
        time.sleep(15)
