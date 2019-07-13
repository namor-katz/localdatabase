#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  localdatabase.py
#
#  Copyright 2018 roman <roman@roman-pc>
# нужно: получить полные пути ко всем файлам.

from peewee import *
import tools
import sys


# define database settings
db = SqliteDatabase('localdatabase.db')

class InfoFile(Model):
    name = CharField()
    full_path = CharField()
    file_hash = CharField()
    file_size = CharField()
    file_type = CharField()
    tag = CharField()
    read = BooleanField()
    double = BooleanField()

    class Meta:
        database = db


# create db and table
db.create_tables([InfoFile])

# getters and setters
def add_values(fname):
    '''принимаем полный путь, получаем инфу, привлекая функции of tools.
    save data in sqlite database'''
    new_value = InfoFile(
        name = fname.split('/')[-1],
        full_path = fname,
        file_hash = tools.return_hash_file(fname),
        file_type = tools.get_file_type,
        tag = None,
        read = 0,
        double = None
    )
    new_value.save()


def get_data(name):
    '''принять имя, отдать всю инфу'''
    pass


if __name__ == '__main__':
    dir_path = sys.argv[1]
    files_list = tools.get_dir_content(dir_path)
    for i in files_list:
        print(i)
