#!/usr/bin/env python
# -*- coding: utf-8 -*-
# CreateTime: 2018-05-24 15:01:41

import os
import time
import tarfile
import logging


LOG_DIR = ['/mnt/log/test/']
FILE_SIZE = 10240 #10M

T = time.strftime("%Y/%m/%d %H:%M", time.localtime())

logging.basicConfig(format='%(asctime)s %(message)s', filename='compress.log', level=logging.INFO, datefmt='%Y/%d/%m %I:%M:%S')


def reduce_files(file_name):
    gz = file_name + '.tar.gz'
    with tarfile.open(gz, "w:gz") as tar:
    	tar.add(file_name)

# not use
def get_file_size(file_path):
	if os.path.getsize(file_path) >= FILE_SIZE:
		return True
	else:
		return False


def truncate_log(abs_path, flist):
	os.chdir(abs_path)
	for f in flist:
		if os.path.isfile(f):
			# logging.info('compress start [%s %s]', abs_path, f)
			logging.info('compress start  [%s]', f)
			reduce_files(f)
			remove_files(f)
			logging.info('compress end [%s]',  f)


def ret_abs_dir(f_path):
	ret = {}
	fs = []
	for root, dirs, files in os.walk(f_path):
		for name in files:
			if not 'tar.gz' in name and '.log.' in name:
				#ret.append(os.path.join(root, name))
				logging.debug('walk to path %s [] file %s', root, name)
				fs.append(name)
				ret[root] = fs
	logging.debug('return dic is %s', ret)
	return ret


def remove_files(file_name):
	if os.path.isfile(file_name):
		os.remove(file_name)

#not use
def ret_file_size(f_list):
	for f in range(len(f_list)):
		if get_file_size(f_list[f]):
			truncate_log(f_list[f])
	return 0


def run(file_dic):
	"""
	input: file_dic is dictory
	"""
	for k,v in file_dic.items():
		logging.debug("input dic key:%s value:%s", k, v)
		truncate_log(k,v)


def main():
	for i in LOG_DIR:
		all_files = ret_abs_dir(i)
		run(all_files)
		#ret_file_size(all_files)


if __name__ == '__main__':
	main()

