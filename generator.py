
import sys

def generate():
    x = 10
    while (x < 50):
        yield x
        x+= 1
    

input = raw_input("Do you want another number: ")
sys.stdout.flush()
input.strip()
input = input.lower()
g = generate()
while True:
    if input == 'yes':
        print next(g)
        sys.stdout.flush()
    else:
        break
    input = raw_input("Do you want another number: ")
    input.strip()

print "Generator exiting !!"
sys.stdout.flush()
