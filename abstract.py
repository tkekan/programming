
from abc import ABCMeta, abstractmethod

class Shape(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, val):
        self.val = val

    def myshape(self):
        pass

class Square(Shape):
    points = 4
    def __init__( self, sides , arg):
        super(Square, self).__init__('genericShape')
        self.sides = sides
        self.sval = arg
    def myshape(self):
        print "My sides are %d and shape is %s: Parent is %s" %(self.sides, self.sval, self.val)

s1 = Square(4, 'square')
s1.myshape()
s2 = Shape(-1)
s1.val = 'Generic Modified Shape'
s1.myshape()
s3 = Square(4, 'tanvirSquare')
s3.myshape()

