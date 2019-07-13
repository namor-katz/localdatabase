#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tools.py
#
#  Copyright 2018 roman <roman@roman-pc>
# берем список файлов, получаем абс пути, получаем хэши
from os import walk, path
from hashlib import md5

p = '/home/roman/gits/localbase'

def return_hash_file(fname):
    '''get selected file, return string md5sum'''
    hash_md5 = md5()
    with open(fname, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def list_files_raw(path_to_dirs):
    '''create list all files, dirs and any objects'''
    f = []
    for i in walk(path_to_dirs):
        f.append(i)
        #f.append('neP')
    return f

a = list_files_raw(p)

def list_selected_file(a=a):
    ''' да, именно это возвращает полные пути.'''
    path_f = []
    for d, dirs, files in a:
        for f in files:
            path1 = path.join(d,f)
            path_f.append(path1)
    return path_f


lf = list_selected_file()
#print(type(lf))
'''
for i in lf:
    print(i)
    a = return_hash_file(i)
    print(a + '\n')

'''
