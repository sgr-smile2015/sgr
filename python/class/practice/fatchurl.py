#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib2
import threading

_lock = threading.Lock()


class FetchUrl(threading.Thread):

    def __init__(self, urls, output, lock):
        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output
        self.lock = lock

    def run(self):
        while self.urls:
            url = self.urls.pop()
            ret = urllib2.Request(url)
            try:
                d = urllib2.urlopen(ret)
            except urllib2.URLError, e:
                print 'url %s is faild: %s' % (url, e.reason)
            #self.lock.acquire()
            with self.lock:
                print 'lock acquire by -- %s' % self.name
                self.output.write(d.read())
                print 'writed done %s' % self.name
                print 'Url %s is fetch: %s' % (url, self.name)
            #self.lock.release()


def main():
    urls1 = ['http://www.baidu.com', 'http://cn.bing.com']
    urls2 = ['http://www.ipin.com', 'http://www.coolshell.cn']
    f = open('out.txt', 'w+')

    t1 = FetchUrl(urls1, f, _lock)
    t2 = FetchUrl(urls2, f, _lock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    f.close()

if __name__ == '__main__':
    main()

