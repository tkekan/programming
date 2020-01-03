import traceback
import time
import signal
import sys


def signal_term_handler():
    print "Signal term handler"
    sys.exit(0)

signal.signal(signal.SIGABRT, signal_term_handler)
def main():
    time.sleep(10)
    a = 1/0
    print "Exiting from maiin in 10 secs..."
    time.sleep(10)

def before():
    time.sleep(2)
    print "Inside before now calliing main"
    time.sleep(5)
    main()

try:
    before()
except Exception as e:
    print "Caught exception: %s" % str(e) 
    print traceback.format_exc()

