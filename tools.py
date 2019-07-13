#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tools.py
#
#  Copyright 2018 roman <roman@roman-pc>
# берем список файлов, получаем абс пути, получаем хэши
import os
import sys
from hashlib import md5
import magic


def return_hash_file(fname):
    '''get selected file, return string md5sum'''
    hash_md5 = md5()
    with open(fname, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()



def get_dir_content(full_path):
    '''принять путь к дире, вернуть ейные полные пути'''
    path_to_files = []
        
    for root, dirs, files in os.walk(full_path):
        for f in files:
            file_path = os.path.join(root, f)
            path_to_files.append(file_path)

        for d in dirs:
            d = os.path.join(root, d)
            #get_dir_content(dir_path)
            print(d)

        return path_to_files


def get_file_size(full_path):
    '''принять полный путь, вернуть размер'''
    return os.path.getsize(full_path)


def get_file_type(full_path):
    ''' принять полный путь, вернуть тип файла.
    если не получилось вернуть отсутствие значения'''
    try:
        file_type = magic.from_file(full_path)
        return file_type
    except:
        return None


if __name__ == '__main__':
    dir_path = sys.argv[1]
    a = get_dir_content(dir_path)
