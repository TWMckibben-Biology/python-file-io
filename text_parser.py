#! /usr/bin/env python3
print('Hello')

import sys
import re


####
#       ="herit" returned just herit
#       ="*herit" and "herit*" returned good hits but not entire words
#       ="\w*herit*\w" grab full words but hits surrounded by -- (ie --inheritance--) cannot have tabs inserted in the write step

wordsearch = "\w*herit*\w"
wordcompiler = re.compile(wordsearch)

with open('origin.txt', 'r') as rf:
    with open ('output_origin.txt', 'w') as wf:
        for line_index, line in enumerate(rf, 1):
            if wordcompiler.findall(line):
                hits = wordcompiler.search(line)
                #print(hits)
                #print(line_index)
                #print({line_index},{hits})
                #print(line_index,hits.group())  This is what I actually want, just need to tab separate and newline
                wf.write("{0}\t{1}\n".format(line_index, hits.group()))
print('Goodbye')
        

if__name__ = '__main__'
