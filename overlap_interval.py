

def overlap(inputs):
    ip = sorted(inputs, reverse = True)
    index = 0
    i = 0
    print ip
    while i < len(ip):
        if index != 0 and ip[index-1][0] <= ip[i][1]:
			#import pdb; pdb.set_trace()
			while index != 0 and ip[index-1][0] <= ip[i][1]:
				left = min(ip[index-1][0], ip[i][0])
				right = max(ip[index-1][1], ip[i][1])
				ip[index-1] = [left,right]
				index -= 1
        else:
			ip[index] = ip[i]
        index += 1
        i += 1	
    return ip[0:index]




inputs = [[8,10], [1,4],[6,7], [5,9], [3,4]]
inputs = overlap(inputs)
print inputs

