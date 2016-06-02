#!/usr/bin/python

"""
Purpose:     process lines matching a defined regex
Usage:       process_lines_with_regex.py [file]
Example:     process_lines_with_regex.py input.txt
Responsible: Stephan Rosenke <r01-571@r0s.de>
License:     CC BY-SA 4.0
Version:     2015-06-02
Based on:    n/a
"""

"""
* set some user serviceable vars
"""
output  = 'output.txt'
#regexe mit re.match haben einen impliziten ^-Anker
regex_a = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun) '
regex_b = '^.*/usr/sbin/mysqld$'

"""
********************************************************************************
*                         DON'T MESS BEHIND THIS LINE
********************************************************************************
"""

"""
* import some modules
"""
from time import strftime, strptime

import re
import sys

"""
* set some non-user serviceable vars
"""
f             = open(sys.argv[1], 'r')
interim       = ''

"""
* define some functions
"""


 
"""
********************************************************************************
************************************* Main *************************************
********************************************************************************
"""

for line in f:
  if re.match(regex_a, line):
    t = strptime(line.rstrip(), '%a %b %d %H:%M:%S %Z %Y')
    line = strftime('%Y-%m-%d %H:%M:%S', t)
    interim = interim + line + ' '
    continue

  if re.match(regex_b, line):
    line = re.sub(' +', ' ', line)
    s = line.split(' ')
    interim = interim + s[2] + ' ' + s[3] + '\n'
    continue

o = open(output, 'w')
o.write(interim)
o.close()

#cleanup
#n/a


"""
************************************ EOF **************************************
"""
