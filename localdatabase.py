#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  localdatabase.py
#
#  Copyright 2018 roman <roman@roman-pc>
# нужно: получить полные пути ко всем файлам.

import os
from tools import *
import logging
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey,  Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

#created db
engine = create_engine('sqlite:///new.db', echo=True)
#обязательно нужно создавать сессию. без неё никак!
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

# define variables
key_words = ['AI', 'algoritms', 'aws', 'bash', 'c', 'c++', 'cryptography',
 'django', 'docker', 'english', 'flask', 'freebsd', 'go', 'golang',
 'haskell', 'java', 'linux', 'machin learning', 'mongodb', 'mysql',
 'oracle', 'orm', 'php', 'postgresql', 'python', 'ruby', 'sql', 'sqlalchemy',
 'sqlite', 'svg', 'unix', 'mobile', 'vba', 'exel']

enable_extension = ['pdf', 'doc', 'djvu', 'txt', 'odt', 'docx', 'epub']
archive_extension = ['zip', 'rar', 'tar', '7z', 'gz', 'bz2']
exclude_extensions = ['mp4', 'mp3']
name_prefix = '1Sf' # для помечания уже отработанных файлов

#define classes
class InfoFile(Base):
    ''' и вот наша таблица с инфо о файле'''
    __tablename__ = 'info_file'
    id = Column(Integer,  primary_key=True)
    name = Column(String,  index=True)
    full_path = Column(String)
    file_hash = Column(String,  index=True)
    file_size = Column(String) # may be, int?
    file_type = Column(String)
    file_lang = Column(String)
    page_count = Column(Integer)
    tag = Column(String)
    notes = Column(String) # это чарфилд или текстфилд?
    read = Column(Boolean)
    double = Column(Boolean)
    assessment = Column(Integer) # 1-5


class Author(Base):
    '''тот же автор, вид сбоку'''
    __tablename__ = 'author'
    id = Column(Integer,  primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Technology(Base):
    __tablename__ = 'technology'
    id = Column(Integer, primary_key=True)
    technology = Column(String)
    level = Column(String)


'''
class Technology2(BaseModel):
    tecnology = CharField(default=None, null=True)
    level = IntegerField(default=None, null=True)
'''
'''
class Book(BaseModel):
    fname_id = ForeignKeyField(InfoFile, related_name='book', unique=False)
    #technology_id = 
    fname = CharField()
    #author = ForeignKeyField(Author, related_name='author', unique=False)
'''

'''
class BrokenFiles(BaseModel):
    name = CharField()
    full_path = CharField()
'''

def get_hash(fname):
    pass


def add_values(farray):
    #проверяем, стоит ли вообще файл парсить.
    new_files = []
    for fname in farray:

        next_step = False
        for i in enable_extension:
            if fname.endswith(i) is True:
                next_step = True

        if next_step is True:
            #print(fname)

            new_value = InfoFile(
                name = fname.split('/')[-1],
                full_path = fname,
                file_hash = return_hash_file(fname),
                file_size = get_file_size(fname),
                file_type = get_file_type(fname),
                file_lang = check_ru_lang(fname),
                page_count = get_file_content(fname)[1],
                tag = None, #get_tag(fname),
                read = False,
                double = None
                                )
            #если размер нулевой, ибо у меня есть битые файлы, не пишем, либо пишем в отдельную таблицу. где только путь
            if new_value.file_size == 0:
                print('no added {}'.format(new_value.name)) #TODOS logging
            else:
                #new_value.save() # this is from peewe
                new_files.append(new_value)

        for i in new_files:
            session.add(i)

    session.commit()

'''
        new_value2 = Book(
            fname_id = InfoFile.get(InfoFile.full_path==fname).id,
            fname = InfoFile.get(InfoFile.full_path==fname).name,
        )
        new_value2.save(force_insert=True)
'''

if __name__ == '__main__':
    # Создание таблицы
    Base.metadata.create_all(engine)
    dir_path = sys.argv[1]
    main_list = []
    for entry in scantree(dir_path):
        main_list.append(entry.path)
    
    add_values(main_list)
