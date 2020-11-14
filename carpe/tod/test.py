#!/usr/bin/env python3
"""test.py"""

import re, sys

# Python read line by line from file.
def read_by_line(filename):
    with open(filename, 'r') as f:
        for line in f:
            print(line)
            
def read_by_line0(filename):
    with open(filename, 'r') as f:
        for line in f:
            #sys.stdout.write(line)
            print(line, end='')
# Python write into file.
def write_into(filename):
    # 'a' -> append()
    # 'w' -> write()
    with open(filename, 'a') as f:
        f.write('hello ysh\n')


def _main():
    readfile = 'testread'
    writefile = 'testwrite'
    read_by_line0(readfile)
    write_into(writefile)
    

_main()
