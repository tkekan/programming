import os
import sys

def walk(top):
    for f in os.listdir(top):
        print f



if __name__ == '__main__':
    walk(sys.argv[1])
