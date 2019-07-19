

def totaltime(tasks, k):
	tdic = {}
	time = 0
	for index in range(0, len(tasks)):
		if tasks[index] not in tdic:
			time += 1
			tdic[tasks[index]] = index
			continue
		else:
			previdx = tdic[tasks[index]]
			if index - previdx < k:
				tdic[tasks[index]] = previdx + k + 1
				time = time + k + (index - previdx)
			else:
				tdic[tasks[index]] = index
				time += 1
			
	print time
	print tdic




tasks = [1,1,2,3,3,2,2,1,1]
totaltime(tasks, 2)
