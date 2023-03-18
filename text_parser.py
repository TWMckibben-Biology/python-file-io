#! /usr/bin/env python3
print('Hello')

import sys
import re

wordsearch = "inheritance"
wordcompiler = re.compile(wordsearch)

with open('origin.txt', 'r') as rf:
    with open ('output_origin.txt', 'w') as wf:
        for line_index, line in enumerate(rf, 1):
            if wordcompiler.findall(line):
                hits = wordcompiler.search(line)
                print(hits)
print('Goodbye')
        

if__name__ = '__main__'
