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


class InfoFile(Model):
    name = CharField()
    path = CharField()
    hash_f = CharField()
    tag = CharField()
    type = CharField()
    read = BooleanField()
    double = BooleanField()

    class Meta:
        database = db

#create db and table
db.create_tables([InfoFile])

def add_values(fname):
    new_value = InfoFile(
    name = fname.split('/')[-1],
    path = fname,
    hash_f = return_hash_file(fname),
    tag = 'No tag',
    type = 'No type',
    read = 'f',
    double = 'f'
    )
    new_value.save()
    
    
camas = InfoFile(
    name ='camasutra',
    path ='no path',
    hash_f = 'no hash',
    tag = 'notag',
    type = 'pdf',
    read = 'f',
    double = 'f'    
)
    

#camas.save()
