#! /usr/bin/env python3
print('Hello')

import sys
import re


####
#       ="herit" returned just herit
#       ="*herit" and "herit*" returned good hits but not entire words

wordsearch = "\w*herit\w*"
wordcompiler = re.compile(wordsearch, re.IGNORECASE)

with open('origin.txt', 'r') as rf:
    with open ('output_origin.txt', 'w') as wf:
        for line_index, line in enumerate(rf, 1):
            if wordcompiler.findall(line):
                hits = wordcompiler.search(line)
                #print(hits)
                #print(line_index)
                #print({line_index},{hits})
                #print(line_index,hits.group())  This is what I actually want, just need to tab separate and newline
                wf.write('line_index\thits.group\n')
print('Goodbye')
        

if__name__ = '__main__'
