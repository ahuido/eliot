#!/usr/bin/env python3
"""clean.py"""

# This is the final python file for cleansing Shelley's work.

import re


def tag(line):
    p_note = re.compile(r'^_\d+.*')
    p_star = re.compile(r"\*\*\*")
    p_blank = re.compile(r'^\s*$')
    p_numbered = re.compile(r'^[A-Z].*(_\d+)$')
    p_numbered_5 = re.compile(r'^[A-Z].*(_5)$')
    p_other = re.compile(r'\d+\.$')

    if p_numbered_5.match(line):
        return 'numbered_5'
    if p_numbered.match(line):
        return 'numbered'
    elif p_blank.match(line):
        return 'blank'
    elif p_star.match(line):
        return 'star'
    elif p_note.match(line):
        return 'note'
    elif line.isupper():
        return 'upper'
    elif p_other.match(line):
        return 'other'
    else:
        return 'verse'
    # This function is not strictly able to recognize corresponding tag.


# This is just for the line number tagged in the tail.
def get_num(numbered_line):
    return int(numbered_line[numbered_line.index('_') + 1:])


def next_numbered(f, line):
    while tag(f[line]) != 'numbered':
        line += 1
    return line


# Returns a list referring the index line.
def get_rough_verse(frag, index):
    four = 1
    back = 1
    while four < 4:
        if tag(frag[index - back]) == 'verse':
            four += 1
            back += 1
        else:
            back += 1
    begin = index - back
    end = 1
    carpe_line = frag[index + end]
    while tag(carpe_line) != 'star':
        if end == len(frag) - index - 1:
            break

        end += 1
    end += index
    carpe_verse = []
    while begin <= end:
        line = frag[begin]
        # if tag(line) == 'verse':
        carpe_verse.append(line)
        begin += 1
    return carpe_verse


# def sieve

def _main_():
    with open('shelley-1', 'r') as fr:
        fragments = [line.rstrip() for line in fr]
        with open('data/clean01', 'w') as fw:
            for i in range(len(fragments)):
                if tag(fragments[i]) == 'numbered_5':
                    verse = get_rough_verse(fragments, i)
                    # for line in verse:
                    #    fw.write('{}\n'.format(line))
                    for line in verse:
                        print(line)


_main_()
