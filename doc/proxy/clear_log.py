#!/usr/bin/env python
# -*- coding: utf-8 -*-
# CreateTime: 2018-05-24 15:01:41

import os
import time

LOG_DIR = ['/mnt/log/', '/mnt/logs/nginx/']
FILE_SIZE = 1073741824 #1G
T = time.strftime("%Y/%m/%d %H:%M", time.localtime())


def get_file_size(file_path):
	if os.path.getsize(file_path) >= FILE_SIZE:
		return True
	else:
		return False

def truncate_log(abs_path):
	if os.path.isfile(abs_path):
		print('[+] %s truncate log: %s' % (T, abs_path))
		os.system("sudo truncate -s 10M %s" % abs_path)

def ret_abs_dir(f_path):
	ret = []
	for root, dirs, files in os.walk(f_path):
		for name in files:
			ret.append(os.path.join(root, name))

	return ret


def ret_file_size(f_list):
	for f in range(len(f_list)):
		if get_file_size(f_list[f]):
			truncate_log(f_list[f])
	return 0


def main():
	for i in LOG_DIR:
		all_files = ret_abs_dir(i)
		ret_file_size(all_files)


if __name__ == '__main__':
	main()

