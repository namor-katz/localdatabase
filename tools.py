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
import PyPDF2


# works files
def return_hash_file(fname):
    '''get selected file, return string md5sum'''
    hash_md5 = md5()
    with open(fname, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def scantree(full_path):
    """Recursively yield DirEntry objects for given directory.
    so 33135038"""
    for entry in os.scandir(full_path):
        if entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)
        else:
            yield entry


def get_file_size(full_path):
    '''принять полный путь, вернуть размер'''
    return os.path.getsize(full_path)


def get_file_type(full_path):
    ''' принять полный путь, вернуть тип файла.
    если не получилось - вернуть отсутствие значения
    хуевенько как то оно определяет. возможно, надо будет поменять'''
    try:
        file_type = magic.Magic(mime=True).from_file(full_path)
        return file_type
    except:
        return None


def check_ru_lang(fname):
    ''' берем имя файла, проверяем все что выше ascii, если есть, 
    возвращаем True, название русское, скорее всего и книга руссиш '''
    check_result = []
    for i in fname:
        if ord(i) > 128:
            check_result.append(1)
    
    if 1 in check_result:
        return 'ru'
    else:
        return 'en'


def get_file_content(fpath):
    '''принять путь к пдфине, извлечь метадату, вернуть титл и число страниц'''
    try:
        with open(fname, 'rb') as f:
            pdf = PyPDF2.PdfFileReader(f)
            info = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
            return info.title, number_of_pages
    except:
        return None, None


if __name__ == '__main__':
    dir_path = sys.argv[1]
    main_list = []
    '''
    for entry in scantree(dir_path):
        main_list.append(entry.path)
    '''
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            file_path = os.path.join(root, f)
            if os.path.exists(file_path):
                main_list.append(file_path)

    print(len(main_list))
