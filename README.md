lyxcitecount
============

Use this to get a count of the number of unique references cited in one or
more [LyX](https://www.lyx.org/) documents. Especially useful when you
have a parent-child document structure and are interested in per-chapter
statistics.

There are two flavours of the program: one written in Bash and the other in
Python. Use whichever is supported in your computing environment; both are
equally short pieces of code. The shell script requires Bash 4.x, `sed` and
`dos2unix`. The interpreted program is compatible with both Python 2 and 3.

You may want to rename or symlink either of the scripts to remove the file
extension for convenience of use. Usage is straightforward:

	~$ lyxcitecount *.lyx
	251
	~$ lyxcitecount Chapter1.lyx Chapter2.lyx
    77

I encourage anyone to try and integrate something like this into the LyX
statistics dialog.
