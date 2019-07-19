

def compare(x,y):
	if x[1] < y[1]:
		return -1
	elif x[1] > y[1]:
		return 1
	if x[1] == y[1]:
		if x[0] < y[0]:
			return -1
		else: return 1
	return 0

def sortbyf(array):
	d = {}
	for items in array:
		d[items] = d.get(items, 0) + 1

	sortedx = sorted(d.items(), cmp = lambda x,y: compare(x,y))
	print "input: ", array
	for items in sortedx:
		print items[0],

array = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
sortbyf(array)
