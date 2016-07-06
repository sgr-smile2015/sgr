#!/usr/bin/python
 
from fabric.colors import red, green
from fabric.context_managers import cd
from fabric.operations import *
from fabric.api import *
 
env.roledefs = {
    'master':['my-master'],
    'slave':['vt9', 'vt7', 'vt2']
    }
#env.hosts = ['my-master', 'vt9', 'vt7', 'vt1', 'vt2']
#env.passwords = {'jay-linux':'123456', 'my-master':'123456'}
env.password = '123456'
 
def color():
    local('ls -l | wc -l')
    print(red("This sentence is red, except for ", bold=True) \
            + green("these words, which are green."))
 
def ctx_mgr():
    with cd('/var/www'):
        run('ls')
 
@roles('master')
def get_sshkey():
    get('/root/.ssh/id_rsa.pub', 'id_rsa.pub.master')
 
@roles('slave')
def put_sshkey():
    with cd('/tmp'):
        put('id_rsa.pub.master', 'id_rsa.pub.master')
        run('cat id_rsa.pub.master >> /root/.ssh/authorized_keys')
 
def do_task():
    execute(get_sshkey)
    execute(put_sshkey)
