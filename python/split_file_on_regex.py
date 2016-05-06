#!/usr/bin/python

"""
Purpose:     split file on a defined regex
Usage:       split_file_on_regex.py [file]
Example:     split_file_on_regex.py input.txt
Responsible: Stephan Rosenke <r01-571@r0s.de>
License:     CC BY-SA 4.0
Version:     2015-05-05
Based on:    n/a
"""

"""
* set some user serviceable vars
"""
regex = '^\r\n'

"""
********************************************************************************
*                         DON'T MESS BEHIND THIS LINE
********************************************************************************
"""

"""
* import some modules
"""
import re
import sys

"""
* set some non-user serviceable vars
"""
counter       = 0
f             = open(sys.argv[1], 'r')
interim       = ''
leadingzeroes = 5

"""
* define some functions
"""


 
"""
********************************************************************************
************************************* Main *************************************
********************************************************************************
"""

for line in f:
  interim = interim + line

  # re.match has implicit ^
  if re.match(regex, line):
    counter_as_string = str(counter)

    output = 'out.'+counter_as_string.zfill(leadingzeroes)+'.txt'

    o = open(output, 'w')
    o.write(interim)
    o.close()

    counter = counter + 1
    interim = ''

#cleanup
#n/a


"""
************************************ EOF **************************************
"""
