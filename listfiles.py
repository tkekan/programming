
import os
import hashlib

def hashfile(path, blockSize = 65535):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blockSize)
    while buf > 0:
        hasher.update(buf)
        buf = fd.read(blockSize)
    fd.close()
    return hasher.hexdigest()

import pdb

def generate(path):
    hashDic = {}
    for root, dirs, files in os.walk(path):
	pdb.set_trace()
        print "Found dir : %s " %root
        for names in files:
            print names, root, dirs
            path =  os.path.abspath(os.path.join(root, names))
	    print "path formed is: ",path
        #for names in dirs:
        #    print os.path.abspath(names)
            #file_hash = hashfile(path)
            #if file_hash in hashDic:
            #    print "Duplicate found : %s" %path
            #else:
            #    hashDic[file_hash] = path

generate("/Users/tkekan/work")
