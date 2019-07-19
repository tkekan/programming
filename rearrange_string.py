import heapq

def rearrange(string):
	tdic = {}
	for items in list(string):
		tdic[items] = tdic.get(items,0) + 1
	h = []
	for items in tdic.items():
		item = [items[1]*-1, items[0]]
		heapq.heappush(h, item)
	prev = [0, '#']
	out = ''
	while len(h):
		item = heapq.heappop(h)
		out = out + item[1]
		
		if prev[0] != 0:
			heapq.heappush(h, prev)

		item[0] = item[0] + 1
		prev = item
	
	if len(out) == len(string):
		print out
		
		
string="aab"
rearrange(string)
