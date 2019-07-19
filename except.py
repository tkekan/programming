import traceback
import sys

def bow():
    try:
        raise NameError
        big  = 10
    except Exception as e:
        print "Caught here " + (repr(e))
        val = traceback.format_exc()
        raise
    finally:
        return big


try:
    ret = bow()
    print "return value: %s" %ret
except Exception as e:
    print (repr(e)) + str(e.message)
