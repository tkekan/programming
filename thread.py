import threading
import time


def func(**kwargs):
    print "Im running func(): " + str(kwargs['a'])
    print "My name is %s" %threading.currentThread().getName()

arg = {'a':1,'b':2}
t1 = threading.Thread(name='tanvir-thread', target=func, kwargs=arg)
t1.setDaemon(True)

t1.start()
time.sleep(5)
t1.join()
print "My name is %s" %threading.currentThread().getName()
