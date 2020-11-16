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
            # sys.stdout.write(line)
            print(line, end='')


# Python write into file.
def write_into(filename):
    # 'a' -> append()
    # 'w' -> write()
    with open(filename, 'a') as f:
        f.write('hello ysh\n')


# Check if a line ends with '_\d+'
def check_end(line):
    # This methods is effective but not efficient.
    # words = line.split()
    # len_words = len(words)
    # last_word = words[len_words - 1]
    # if last_word[0] == '_' and last_word[1:].isdigit():
    #    return True

    # This method is effective and efficient.
    if len(line) < 5:
        return False
    elif ((line[-1].isdigit() and line[-2] == '_')
          or (line[-2].isdigit() and line[-3] == '_')
          or (line[-3].isdigit() and line[-4] == '_')
          or (line[-4].isdigit() and '_' == line[-5])):
        return True
    else:
        return False


def test_check_end():
    with open('data/v1') as f:
        for line in f:
            if check_end(line):
                print(line, end='')
            else:
                continue


def get_num(checked_line):
    tmp = checked_line.split()
    list_len = len(tmp)
    num = int(tmp[list_len - 1][1:])
    return num


# Print several lines before recognized line.
def print_between():
    with open('data/v1') as f:
        times = 0
        for line in f:
            line = re.sub('[A-Z][A-Z]+.*', '', line)
            line = re.sub('^_\d+.*', '', line)
            line = re.sub(r'^\n$', '', line)
            if check_end(line):
                times = 5
                print(line, end='')
            elif times > 0:
                times = times - 1
                print(line, end='')


# Print lines ends with '_\d+'.
def step1():
    with open('data/v1') as f:
        for line in f:
            tmp = line.split()
            list_len = len(tmp)
            if list_len != 0 and tmp[list_len - 1][0] == '_':
                # print(tmp[list_len-1])
                # line = re.sub(r'\s+_\d+', '', line)
                print(line, end='')


# Test get_num() function.
def test_get_num(f):
    for line in f:
        if check_end(line):
            print(get_num(line))
        else:
            continue

def check_ending_segment(line_with_num):
    with open('data/v1') as f:
        lines = [line.rstrip() for line in f]


def _main_():
    # readfile = 'data/testread'
    # writefile = 'data/testwrite'
    # read_by_line0(readfile)
    # write_into(writefile)
    with open('data/v1') as f:
        test_get_num(f)
    f.close()


_main_()
