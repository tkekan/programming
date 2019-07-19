
class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None


def addnumbers(root1, root2):
	num1 = []
	num2 = []
	while root1:
		num1.append(root1.val)
		root1 = root1.next
	
	while root2:
		num2.append(root2.val)
		root2 = root2.next
	
	total = 0
	carry = 0
	res = ''
	while len(num1) or len(num2):
		n1 = 0
		n2 = 0
		if len(num1):
			n1 = num1.pop()
		if len(num2):
			n2 = num2.pop()

		total = n1 + n2 + carry
		carry = total / 10
		val = total % 10
		res = str(val) + res

	if carry > 0:
		res = str(carry) + res

	print "\nSum is : %s" %res


def addnumbersrec(root1, root2):
	if root1.next == None and root2

root1 = Node(6)
root1.next = Node(7)
root1.next.next = Node(3)
root1.next.next.next = Node(9)

root2 = Node(9)
root2.next = Node(7)
#root2.next.next = Node(3)
#root2.next.next.next = Node(9)

addnumbersrec(root1, root2)

addnumbers(root1, None)
addnumbers(None, root2)
addnumbers(None, None)
addnumbers(root1, root2)

root2.next.next = Node(3)
root2.next.next.next = Node(9)

addnumbers(root1, root2)


