
import os
import sys
import pdb


bufsize = 8192
fname = sys.argv[2]
maxlines = int(sys.argv[1])
fsize = os.stat(fname).st_size

line = 0
with open(fname) as f:
    f.seek(0,2)
    position = endf = f.tell()
    while position >= 0:
	f.seek(position,0)
	char = f.read(1)
	if char == '\n':
	    line += 1
	if line > maxlines:
	    break

        position -= 1

    if position < 0:
	f.seek(0,0)
    data = f.readlines()
    print (data)
