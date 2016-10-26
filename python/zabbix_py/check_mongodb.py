#! /usr/bin/python
#Auth:lol
#function:check process_nameor check process_port
#date:2016-8-81
  
import os
import sys
import commands
  
def help():
	print "Usage:  "
	print "       %s process_name [process_port]"%sys.argv[0]
	print "Example: "
	print "       %s mysql         ;If the process_nameexists, output 1, otherwise 0"%sys.argv[0]
	print "       %s nginx  80     ;If the process_port exists, output 1,otherwise 0"%sys.argv[0]
	print "       %s mysql  3306 "%sys.argv[0]
  
def check_process_name():
	process_num = commands.getstatusoutput(" ps -ef|grep -v grep|grep -v %s | grep -v '\[%s\]'|grep %s|wc -l " %(sys.argv[0],sys.argv[1],sys.argv[1]))
	#print process_num
	if not process_num[1]:
		print "0"
		return
	if int(process_num[1]) >= 1:
		print "1"
	else:
		print "0"

def check_process_port():
	process_num=commands.getstatusoutput("netstat -lnt|grep -v grep|grep ':%s '|wc -l" %sys.argv[2])
	if int(process_num[1]) >=1:
		print "1"
	else: 
		print "0"
  
def check_mongodb_connect():
	process_num=commands.getstatusoutput("mongostat -h 192.168.3.32 -u ipin -p xxoo --authenticationDatabase admin -n 1 | awk '{ if($16~/^([0-9])+$/) {print $16}}'")
	print process_num
	if int(process_num[1]) >=1:
		print process_num
	else:
		print "fuck"

###start execute
print sys.argv

if sys.argv[1] == 'mongodb':
	check_mongodb_connect()
	sys.exit()
elif len(sys.argv) == 2:
	check_process_name()
	sys.exit()
elif len(sys.argv) == 3:
	check_process_port()
	sys.exit()
else:
	help()
	sys.exit()
