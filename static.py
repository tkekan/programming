


class O:
    def counter(self):
        self.count = 0;
        if self.count != 10:
            self.count += 1
            self.counter()
        else:
            print "Counter reached 10"
            return


o = O()
O.counter.count = 0
o.counter()
