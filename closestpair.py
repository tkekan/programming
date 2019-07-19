


def closest(arr, x):
	low = 0
	high = len(arr) - 1
	minDif = float('inf')
	pair = []
	while low < high:
		s = arr[low] + arr[high]
		sdif = abs(s - x) 
		if sdif < minDif:
			minDif = sdif
			pair = [arr[low], arr[high]]
		if s > x:
			high -= 1
		elif s < x:
			low += 1
	return pair
			   

#arr = [10,22,28,29,30,40]
arr = [1, 3, 4, 7, 10]
print(closest(arr, 15))
