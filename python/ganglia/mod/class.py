#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import os
import sys
import threading
import time

descriptors = list()
Desc_skel = {}
_conf = {}
log_seek = {}
_Worker_Thread = None
# synchronization lock
_Lock = threading.Lock()
next_pos = 0


def file_to_dic(source):
    ret = list()
    with open(source) as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            #print '-->%s' % line
            l = line.split(':')
            ret.extend(l)
    return dict(zip(ret[0::2], ret[1::2]))


class UpdateMetricThread(threading.Thread):

    def __init__(self, param):
        threading.Thread.__init__(self)
        self.running = False
        self.shuttingdown = False
        self.refresh_rate = 10
        if "refresh_rate" in param:
            self.refresh_rate = int(params["refresh_rate"])
        self.metric = {}

    def shutdown(self):
        self.shuttingdown = True
        if not self.running:
            return
        self.join()

    def run(self):
        self.running = True

        while not self.shuttingdown:
            _Lock.acquire()
            self.update_metric()
            _Lock.release()
            time.sleep(self.refresh_rate)

        self.running = False

    def update_metric(self):
        pass

    @classmethod
    def metric_f(cls, app, path):
        global next_pos
        _Lock.acquire()
        count = 0
        target_file = open(path, 'rb')
        error = 'ERROR'
        target_file.seek(log_seek[app], 0)
        while True:
            start = target_file.read(8192 * 1024)
            if not start:
                break
            count += start.count(error)
            log_seek[app] = target_file.tell()
        target_file.close()
        _Lock.release()
        return int(count)


def metric_init(param):
    global descriptors, Desc_skel, _Worker_Thread
    # initialize skeleton of descriptors
    Desc_skel = {
        'name': 'xxx',
        'call_back': 'xxx',
        #'call_back': metric_of,
        'time_max': 90,
        'value_type': 'uint',
        'units': 'Num',
        'slope': 'both',
        'format': '%u',
        'description': 'xxx',
        'groups': 'app log'
        }

    if "refresh_rate" not in param:
        param["refresh_rate"] = 10

    # IP:HOSTNAME
    if "spoof_host" in params:
        Desc_skel["spoof_host"] = params["spoof_host"]
    for app, path in _conf.iteritems():
        #print app, path
        descriptors.append(create_desc(Desc_skel, {'name': 'log_' + app,
                                                   'call_back': lambda name, ap=app, ph=path: metric_of(ap, ph),
                                                   'description': 'Find error in ' + app}))

    _Worker_Thread = UpdateMetricThread(params)
    _Worker_Thread.start()

    return descriptors


def create_desc(sk, prop):
    dic = sk.copy()
    for k, value in prop.iteritems():
        dic[k] = value
    return dic


def metric_of(app, path):
    return _Worker_Thread.metric_f(app, path)


def metric_cleanup():
    _Worker_Thread.shutdown()

if __name__ == '__main__':
    _conf = file_to_dic('config')
    for e in _conf:
        log_seek[e] = 0

    try:
        params = {}
        metric_init(params)
        while True:
            for d in descriptors:
                v = d['call_back'](d['name'])
                print ('value for %s is '+d['format']) % (d['name'],  v)
            time.sleep(5)
    except KeyboardInterrupt:
        time.sleep(0.2)
        os._exit(0)
    except:
        print sys.exc_info()[0]
        raise
