#! /usr/bin/python

import paramiko

def server_cmd(serverip):
    ip = serverip
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, "root", "123456")
    stdin,stdout,stderr = ssh.exec_command("cat ~/a.py >> .ssh/authorized_keys")
    stdin,stdout,stderr = ssh.exec_command("rm a.py")
    print stdout.readlines()
    ssh.close()

remote = '/home/ipin/a.py'
local = '/home/sgr/.ssh/id_rsa.pub'

iplist = [
"192.168.1.46",
#"192.168.1.83"
]
for ip in iplist:
    server = paramiko.Transport(ip,"22")
    server.connect(username = "root", password = "123456")
    stfp = paramiko.SFTPClient.from_transport(server)
    stfp.put(local,remote)
    server.close()
    server_cmd(ip)
