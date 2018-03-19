#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import tarfile
import os
import glob


def get_files_list():
    return glob.glob("./*.log.2017-11*")


def reduce_files(file_name):
    gz = file_name + '.tar.gz'
    tar = tarfile.open(gz, "w:gz")
    tar.add(file_name)
    tar.close()


def remove_files(file_name):
    os.remove(file_name)


if __name__ == '__main__':
    for f in get_files_list():
        print(f)
        reduce_files(f)
        remove_files(f)
