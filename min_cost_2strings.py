
def returncost(s1,s2, costl):
	q = []
	cost = costl
	q.append([0,s1])
	results = float('inf')
	while len(q):
		#import pdb; pdb.set_trace()
		item = q[0]
		q = q[1:]
		check = item[1]
		for items in costl.items():
			change = False
			val = items[1]
			check = list(item[1])
			cost = 0
			for index in range(0, len(s2)):
				if check[index] == s2[index]:
					continue
				if check[index] != s2[index] and (s2[index] in val and check[index] in val):
					check[index] = s2[index]
					cost += items[0]
					change = True
					continue
			if change == True and check != list(s2):
				q.append([cost,''.join(check)])
				change = False
			if check == list(s2):
				results = min(results, cost)

	print results

s1 = "222" 
s2 = "111"
a = 20 
b = 30 
c = 40 
d = 10
costl = {a: ['1','2'], b: ['2','3'], c: ['3','1']}
returncost(s1,s2, costl)
