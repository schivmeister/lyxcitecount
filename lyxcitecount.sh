#!/bin/bash

# -----------------------------------------------------------------------------
# lyxcitecount.sh: counts the number of references cited in LyX [1] documents
# Requires: bash 4.x (due to bashism), sed, dos2unix (by Erwin Waterlander) [2]
# -----------------------------------------------------------------------------
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
# [2] http://waterlan.home.xs4all.nl/dos2unix.html
# -----------------------------------------------------------------------------

[[ -z "$1" ]] && echo "usage: $(basename $0) <file1> <file2> ..." && exit 1

for i in "$@"; do
	[[ ! -f "$i" ]] && echo "error: '$i' is not a file" && exit 1
done

# this here requires EOL to be UNIX because we match '$'
# without it our regex would be weaker than it already is
REkey='^key "[aA-zZ|0-9].*"$'

# so we convert first
for i in "$@"; do
	cp "$i" "$i.lcctmp" # and we assume .lcctmp is unique - very unscientific, but KISS
	# pure *NIXers may remove or comment out the following line
	which dos2unix &> /dev/null && dos2unix -q "$i.lcctmp"
	tmpfiles+=("$i.lcctmp") # and also we need another array to hold these
done

# for the one-liner magic (broken up for convenience)
grep "$REkey" "${tmpfiles[@]}" | sed -e 's/.*://' \
	-e 's/key //' \
	-e 's/"//g' \
	-e 's/,/\n/g' | sort -u | wc -l

# and we're done; remove temp files
rm *.lcctmp # so sorry if you actually had files with this "extension"
