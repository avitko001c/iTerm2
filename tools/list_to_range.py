#!/usr/local/bin/python
from __future__ import print_function
from builtins import input
from builtins import str
from builtins import hex

import itertools

def get_ranges(i):
    for a, b in itertools.groupby(enumerate(i), lambda x_y: x_y[1] - x_y[0]):
        b = list(b)
        yield b[0][1], b[-1][1]

contents = []
while True:
    try:
        line = input("")
    except EOFError:
        break
    contents.append(line)

numbers = [int(x, 16) for x in contents]
for x in get_ranges(numbers):
  print("[set addCharactersInRange:NSMakeRange(%s, %s)];" % (hex(x[0]), str(x[1] - x[0] + 1)))
