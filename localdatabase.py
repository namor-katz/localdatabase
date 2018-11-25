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
    hash = CharField()
    tag = CharField()
    type = CharField()
    read = BooleanField()

    class Meta:
        database = db
        
db.connect()

