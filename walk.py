#!/Users/tkekan/.pyenv/shims/python
import pprint

from os import walk
mypath = './'
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    print(id(f))
    f = f.extend(filenames)

print(f)
print(id(f))
