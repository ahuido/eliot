#!/usr/bin/env python3
"""diem.py"""
import sys, re


# The text file is stored in a list, so all these following functions are list-based.
def ysh00(line):
    if len(line) < 5:
        return False
    elif ((line[-1].isdigit() and line[-2] == '_')
          or (line[-2].isdigit() and line[-3] == '_')
          or (line[-3].isdigit() and line[-4] == '_')
          or (line[-4].isdigit() and '_' == line[-5])):
        return True
    else:
        return False


# Tag the line and return which
def ysh01(line):
    p_note = re.compile(r'^_\d+.*')
    p_star = re.compile(r"\*\*\*")
    # This regex: '^' marks the start of a line, and '\s' space character, '*' means none or many '\s', '$' marks the
    # end of this line.
    p_blank = re.compile(r'^\s*$')
    # ysh00(line) acts in the same manner.
    p_numbered = re.compile(r'^[A-Z].*(_\d+)$')
    p_numbered_5 = re.compile(r'^[A-Z].*(_5)$')
    p_other = re.compile(r'\d+\.$')
    if p_numbered_5.match(line):
        return 'numbered_5'
    if p_numbered.match(line):
        return 'numbered'
    # elif len(line) == 0:
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


# Extract line number of type INT from numbered line.
def ysh02(line):
    return int(line[line.index('_') + 1:1])


# Returns the pair of beginning and ending line numbers.
def get_foot_pair(l, foot_l5):
    foot = 1
    back = 1
    while foot < 4:
        if ysh01(l[foot_l5 - back]) == 'verse':
            foot += 1
            back += 1
        else:
            back += 1
    begin = foot_l5 - foot
    end = 1
    while ysh01(l[foot_l5 + end]) != 'star':
        end += 1
    end = foot_l5 + end
    return begin, end


# Return a list of line numbers denoting the starting line of fragments.
# Or maybe return a list with all fragments contained.
# This function accept a list variable, in that sense, an array.
# So `percy' is an array.
def ysh03(percy):
    # the `tmp' list is used to store temporary single fragments.
    tmp = []
    shelley = []
    for i in range(len(percy)):
        if ysh01(percy[i]) == 'numbered_5':
            l1 = get_foot_pair(percy, i)
            begin = l1[0]
            end = l1[1]
            print(percy[begin:end], sep='\r\n')
        # else:

    return shelley


def ysh99():
    line = 'fare you well people of czar _99'
    print(int(line[line.index('_') + 1:]) + 1)


def ysh98(line):
    if ysh01(line) == 'other':
        print(line)


# Test of extracting the beginning segments.
def ysh97(l_shelley):
    for line in l_shelley:
        if ysh01(line) == 'numbered_5':
            verse_begin = []
            foot = l_shelley.index(line)
            verse = 1
            back = 1
            print()
            verse_begin.insert(5, line)
            while verse < 5:
                if ysh01(l_shelley[foot - back]) == 'verse':
                    verse_begin.insert((0 - back), l_shelley[foot - back])
                    # print('{:<7}{}'.format((foot - back), l_shelley[foot - back]))
                    verse += 1
                    back += 1
                else:
                    back += 1
            # print('{:<7}{}'.format(foot, line))
            for whatever in verse_begin:
                print(whatever)
            # l_begin.append([(foot - back), l_shelley[foot - back]])
            # l_begin.append([(foot - back), foot])
    # for whatever in l_begin:
    #    print(l_shelley[whatever[0]:whatever[1]])


def ysh96(l_shelly):
    num_verse = 0
    for line in l_shelly:
        if ysh01(line) == 'numbered_5':
            foot = l_shelly.index(line)
            back = 0
            verse = 1
            while verse < 5:
                print(foot, l_shelly[foot])
            num_verse += 1
    # This is the total fragments in this book.
    print(num_verse)


def _main_():
    with open('shelley-1', 'r') as f_1:
        shelley_1 = [line.rstrip() for line in f_1]
        # ysh03(shelley_1)
        for line in shelley_1:
            if line.isupper():
                print(line)
        # for line in shelley_1:
        #    ysh98(line)
    # i = 0
    # for line in shelley_1:
    # words = line.split()
    # num_words = len(words)
    # if num_words != 0:
    #    print('{:<5} {}'.format(num_words, line))
    # print('{:<3}>>{}<<'.format(len(line), line))
    # if ysh01(line) == 'blank':
    #    print(line)
    # ysh99()


_main_()
