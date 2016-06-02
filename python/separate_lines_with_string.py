#!/usr/bin/python

"""
Purpose:     separate lines matching a defined string
Usage:       separate_lines_with_string.py [file]
Example:     separate_lines_with_string.py input.txt
Responsible: Stephan Rosenke <r01-571@r0s.de>
License:     CC BY-SA 4.0
Version:     2015-06-02
Based on:    n/a
"""

"""
* set some user serviceable vars
"""
output_prefix = 'output'
output_suffix = '.csv'

"""
********************************************************************************
*                         DON'T MESS BEHIND THIS LINE
********************************************************************************
"""

"""
* import some modules
"""
import sys

"""
* set some non-user serviceable vars
"""
f       = open(sys.argv[1], 'r')
interim = ''
string  = ''

"""
* define some functions
"""


 
"""
********************************************************************************
************************************* Main *************************************
********************************************************************************
"""

for line in f:
  s = line.split( )

  if ((string != s[0]) and (string != '')):
    output = output_prefix + '_' + string + output_suffix

    o = open(output, 'w')
    o.write(interim)
    o.close()

    interim = ''

  interim = interim + line

  string = s[0]

# for writing out last iteration
output = output_prefix + '_' + string + output_suffix

o = open(output, 'w')
o.write(interim)
o.close()

#cleanup
#n/a


"""
************************************ EOF **************************************
"""
