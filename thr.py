import time
from threading import Thread,current_thread
from threading import RLock

def myfunc():
    print "Entered myfunc()"
    mutex.acquire()
    time.sleep(1)
    print "Thread: %s" %current_thread()
    time.sleep(10)
    print "Releasing the lock"
    mutex.release()


mutex = RLock()
t1 = Thread(target=myfunc, name="thread-1")
t2 = Thread(target=myfunc, name="thread-2")
t1.start()
t2.start()
time.sleep(1)
print "Main releasing the lock"
mutex.release()

print "main loop thread blocked here..."
