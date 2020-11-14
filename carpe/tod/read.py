#!/usr/bin/env python
"""read.py"""

import re, sys

# This function is destinied to open files under specific directory recursively.
# open_file(dirname)
# File 'v1' is the vol1 of The Complete Work by Shelley. And so are 'v2' and 'v3'.


f_v1 = open('v1')
f_v2 = open('v2')
f_v3 = open('v3')

def super_line():
    haha_line = re.sub(r'\s', " ", str(f_v1))
    print(haha_line)
    
def test_tod():
    count  = 0
    for line in f_v1:
        count = count + 1
        #if count == 20:
        #    break
        #else:
        #    print(line)
        if line == r'CONTENTS.\r\n':
            break
        else:
            print(count, line)


f_v11 = open('v11', 'w')
f_v11.write(f_v1.read().replace('\r\n', " "))
