#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  без имени.py
#  
#  Copyright 2018 roman <roman@roman-pc>
#  

from peewee import *

db = SqliteDatabase('localdatabase.db')

class Info_file(Model):
    name = Charfield()
    path = Charfield()
    hash = 
    tag = 
    type = 
    read = 
    
