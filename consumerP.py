from threading import Thread, Lock, Condition
import time
import random

queue = []
lock = Lock()
cv = Condition()

class Producer(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id
    def run(self):
        global queue
        while True:
            cv.acquire()
            val = random.randint(1,1000)
            print "Producer %d generated : %d" %(self.id, val)
            queue.append(val)
            cv.notifyAll()
            cv.release()
            time.sleep(random.random())

class Consumer(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

    def run(self):
        global queue
        while True:
            cv.acquire()
            while True and  len(queue) <= 0:
                print "Nothing in queue, consumer %d is waiting..." % self.id
                cv.wait()
            print "Producer added, consumer %d continuing..." %self.id
            val = queue[0]
            queue = queue[1:]
            print "Consumer id : %d consumed %d" %(self.id, val)
            cv.release()
            time.sleep(random.random())



p1 = Producer(1)
p2 = Producer(2)
p1.daemon = True
p2.daemon = True
c1 = Consumer(1)
c2 = Consumer(2)
c3 = Consumer(3)
c4 = Consumer(4)
c1.daemon = True
c2.daemon = True
c3.daemon = True
c4.daemon = True
c1.start()
c2.start()
c3.start()
c4.start()
time.sleep(2)
p1.start()
p2.start()
while True:
    time.sleep(1)
