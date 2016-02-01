#!/usr/bin/env python

"""
Merge function for 2048 game.
"""

def remzero(line):
    """
    Function that moves all zeros to end in a list.
    """
    origlen = len(line)
    line[:] = filter(None, line)
    line.extend([0] * (origlen - len(line)))
    return line

def add(line):
    """
    Function that add consecutive same elements in list.
    """
    for dummy_i in range(0, len(line)):
        if dummy_i+1 < len(line):
            if  line[dummy_i] == line[dummy_i+1]:
                line[dummy_i] += line[dummy_i+1]
                line[dummy_i+1] = 0
    return line

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    line_result = list(line)
    return remzero(add(remzero(line_result)))


#print merge([2,0, 2,4])
#print merge([0,0,2,2])
#print merge([2,2,0,0])
#print merge([2,2,2,2,2])
#print merge([8,16,16,8])
