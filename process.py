from subprocess import Popen, PIPE
import traceback
import shlex
import os
import sys

cmd = 'python generator.py'
args = shlex.split(cmd)
try:
    p1 = Popen(args, shell= False, stdout = PIPE, stdin = PIPE)
    if p1.returncode != 0:
	pass
        #raise Exception("Subprocess failed!")
except Exception as e:
    print "Encountered exception:", repr(e) 
    traceback.print_exc()
    sys.exit()


while True:
    if p1.poll() != None:
        break
    ask = raw_input("Next: ")
    if ask != 'yes':
        print "coming out"
        p1.stdin.write(ask + "\n")
        p1.stdin.flush()
        break
    p1.stdin.write(ask + "\n")
    p1.stdin.flush()
    response = p1.stdout.readline()
    print response




stdout, stderr = p1.communicate()
print "Generator stopped with: " ,stdout
