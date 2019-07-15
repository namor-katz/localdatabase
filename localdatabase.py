#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  localdatabase.py
#
#  Copyright 2018 roman <roman@roman-pc>
# нужно: получить полные пути ко всем файлам.

from peewee import *
from tools import *

db = SqliteDatabase('localdatabase.db')


class BaseModel(Model):
    class Meta:
        database = db


class InfoFile(BaseModel):
    name = CharField()
    full_path = CharField()
    file_hash = CharField()
    file_size = CharField()
    file_type = CharField(default=None, null=True)
    file_lang = CharField(default=None, null=True)
    page_count = CharField(default=None, null=True)
    tag = TextField(null=True)
    notes = TextField(default=None, null=True)
    read = BooleanField(default=False)
    double = BooleanField(default=False)


class Author(BaseModel):
    name = CharField(default=None, null=True)


class Technology(BaseModel):
    tecnology = CharField(default=None, null=True)
    level = IntegerField(default=None, null=True)


class Book(BaseModel):
    
    fname_id = ForeignKeyField(InfoFile, related_name='book', unique=False)
    fname = CharField()
    #author = ForeignKeyField(Author, related_name='author', unique=False)


#create db and table
#db.create_tables([InfoFile, Author, Technology, Book])

def add_values(fname):
    print(fname)
    
    new_value = InfoFile(
    name = fname.split('/')[-1],
    full_path = fname,
    file_hash = return_hash_file(fname),
    file_type = get_file_type(fname),
    file_lang = check_ru_lang(fname),
    file_size = get_file_size(fname),
    tag = None,
    read = 0,
    double = 0
    )
    new_value.save()


    new_value2 = Book(
        fname_id = InfoFile.get(InfoFile.full_path==fname).id,
        fname = InfoFile.get(InfoFile.full_path==fname).name,
    )
    new_value2.save(force_insert=True)


if __name__ == '__main__':
    db.create_tables([InfoFile, Author, Technology, Book])
    dir_path = sys.argv[1]
    main_list = []
    for entry in scantree(dir_path):
        main_list.append(entry.path)

    for i in main_list:
        add_values(i)
