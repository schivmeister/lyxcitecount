#!/usr/bin/python
# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------------
# lyxcitecount.py: counts the number of references cited in LyX [1] documents
# Requires: Python 2.4 or newer (including Python 3)
# ---------------------------------------------------------------------------
# Copyright (c) 2013 Rashif Ray Rahman <schiv@archlinux.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------
# [1] https://www.lyx.org/
# -----------------------------------------------------------------------------

from sys import argv as sargv, exit as sexit
from os.path import basename, isfile
from re import compile as cregexp

if len(sargv) < 2:
	print("usage: "+basename(sargv[0])+" <file1> <file2> ...")
	sexit(1)

# prepare the regex to match relevant lines
REkey = cregexp(r'^key "[aA-zZ|0-9].*"$')
matches = [] # and store them later in an array

for arg in sargv[1:]:
	if not isfile(arg):
		print("error: '"+arg+"' is not a file")
		sexit(1) # just exit if even one arg is invalid

	# looping through each valid file...
	lyxfile = open(arg,'r')
	for line in lyxfile.readlines():
		# first, remove newline
		line = line.strip() # because python2 cannot match '$' if EOL=CRLF
		if REkey.match(line):
			# and begin removing unnecessary chars from this matching line
			line = line.replace("key ","")
			line = line.replace('"',"")
			# then save the modified line for our use
			matches.append(line)

# now split the comma-separated citations into their own list items
# (to tell you the truth, these functional methods are all magic to me)
#matches = [i.split(',', 1)[0] for i in matches] # works but less understandable
matches = [i for line in matches for i in line.split(',')]

# and finally sort the list while removing duplicates
matches = sorted(set(matches))

print(len(matches))
