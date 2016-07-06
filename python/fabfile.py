#! /usr/bin/env python
import os
import re
import time
#from datetime import datetime
from fabric.api import *

env.user = 'ipin'
env.sudo_user = 'root'
env.hosts = ['192.168.1.46']

#ltime = time.strftime("%Y%m%d %H%M%S",time.localtime())
ltime = time.strftime("%Y%m%d",time.localtime())

_TAR_FILE = "source." + ltime + ".tar.gz"

def build():
	include = [ 'src', 'txt','index.html']
	exclude = [ '*.py','logs']
	local('rm -f ./%s' % _TAR_FILE)
	with lcd(os.path.join(os.path.abspath('.') ,'www')):
		cmd = [ 'tar' , '-cvf' , './%s' % _TAR_FILE]
		cmd.extend(['--exclude=%s' % ex for ex in exclude])
		cmd.extend(include)
		local(' '.join(cmd))

_TEMP_TAR = '/tmp/%s' % _TAR_FILE
_BASE_DIR = '/home/ipin/'

def deploy():
#	newdir = 'www_%s' % datetime.now().strftime('%Y%m%d')
	newdir = 'www_%s' % ltime
	run('rm -f %s' % _TEMP_TAR)
	put('www/%s' % _TAR_FILE, _TEMP_TAR)
	with cd(_BASE_DIR):
		sudo('mkdir %s' % newdir)
	with cd('%s/%s' % (_BASE_DIR, newdir)):
		sudo('tar xvf %s' % _TEMP_TAR)
	with cd(_BASE_DIR):
		sudo('rm -f www')
		sudo('ln -sf %s www' % newdir)
		sudo('chown www-data:www-data www')
		sudo('chown -R ipin:ipin %s ' % newdir)

	with settings(warn_only=True):
		sudo('supervisorctl restart redis')

