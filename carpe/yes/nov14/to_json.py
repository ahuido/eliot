#!/usr/bin/env python
"""to_json.py"""

import json, sys, re

f_vol1 = 'v1'
def read_until_end():
    with open(f_vol1, 'r') as vol1:
        for line in vol1:
            print(str(line))
    vol1.close()
def read_until_content():
    with open(f_vol1, 'r') as vol1:
        count = 1
        for line in vol1:
            #if line.split()[0] == 'CONTENTS':
            #    print(str(line))
            #words = line.split()
            #count = count + 1
            #print('{} : {} : {}'.format(count, len(words), words))

            tmp = line.split()
            if len(tmp) == 0:
                continue
            elif tmp[0] == 'CONTENTS.':
                break
            else:
                line = re.sub('\r\n', '', line)
                print(str(line))

def read_content():
    with open(f_vol1, 'r') as vol1:
        count = 1
        star = 0
        for line in vol1:
            tmp = line.split()
            if len(tmp) == 0:
                continue
            elif len(tmp) == 1 and tmp[0] == 'CONTENTS.':
                line = re.sub('\r\n', '', line)
            else:
                print(line)
            if tmp[0] == '***':
                break
    

def read_test():
    with open(f_vol1, 'r') as vol1:
        count = 1
        for line in vol1:
            #if line.split()[0] == 'CONTENTS.':
            #    print(str(line))
            words = line.split()
            count = count + 1
            print('{} : {} : {}'.format(count, len(words), words))


#read_until_content()
read_content()
