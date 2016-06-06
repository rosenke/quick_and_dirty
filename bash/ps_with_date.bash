#!/bin/bash

# Purpose:	ps_with_date.bash
# Usage:	ps_with_date.bash
# Example:	ps_with_date.bash
# Responsible:	Stephan Rosenke <r01-571@r0s.de>
# License:	CC BY-SA 4.0
# Version:	2016-05-24
# Based on:	n/a

################################################################################
# set some user serviceable vars                                               #
################################################################################


################################################################################
################################################################################
######################### DON'T MESS BEHIND THIS LINE ##########################
################################################################################
################################################################################

################################################################################
# set some non-user serviceable vars                                           #
################################################################################

# unset LANG if you parse stdout-put of your commands for preventing problems
# with unanticipated languages
unset LANG

date=$(date +%Y-%m-%d)
file="${HOME}/$(basename ${0} .bash)_${date}.txt"

################################################################################
# define some functions                                                        #
################################################################################



################################################################################
################################################################################
##################################### Main #####################################
################################################################################
################################################################################

date >>"${file}"
w >>"${file}"
ps faux -ww >>"${file}"

#cleanup



################################################################################
##################################### EOF ######################################
################################################################################

