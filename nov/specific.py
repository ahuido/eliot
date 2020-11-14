#!/usr/bin/env python
"""specific"""
import re

pre00 = 'create database eliot;'
pre01 = 'create table poet ('
#        'id          smallint,'
 #       'given_name  varchar(15),'
  #      'middle_name varchar(15),'
   #     'family_name varchar(15),'
    #    'born        date,'
     #   'died        date);'


pop10 = 'insert into poet (given_name) values ('
pop20 = 'insert into poet (given_name, family_name) values ('
pop30 = 'insert into poet (given_name, middle_name, family_name) values ('

def _pop_poet():
    with open('poet_list') as pl:
        i = 1
        for line in pl:
            line = re.sub(r', ', ' ', line)
            poet = line.split()
            if len(poet) == 1:
                gn = poet[0].capitalize()
                # name = str(gn)
                pop = str('{} "{}", "{}" );'.format(pop10, i, gn))
            elif len(poet) == 2:
                fn = poet[0].capitalize()
                gn = poet[1].capitalize()
                # name = str('{} {0} {1}'.format(gn, fn))
                pop = str('{} "{}", "{}", "{}" );'.format(pop20, i, gn, fn))
            elif len(poet) == 3:
                fn = poet[0].capitalize()
                mn = poet[1].capitalize()
                gn = poet[2].capitalize()
                # name = str('{} {0} {1} {2}'.format(gn, mn, fn))
                pop = str('{} "{}", "{}", "{}", "{}" );'.format(pop30, i, gn, mn, fn))
            print(pop)
            i = i + 1

_pop_poet()
