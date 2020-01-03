

def median(arr1, arr2):
    if len(arr1) > len(arr2):
        return median(arr2, arr1)

    x = len(arr1)
    y = len(arr2)
    low = 0
    high = x - 1
    while low <= high:
        partx = low + ((high-low) / 2)
        party = (x + y+1) / 2 - partx
        
        maxleftx = (arr1[partx-1],float('-inf')) [partx == 0]
        maxlefty = (arr2[party-1],float('-inf')) [party == 0]

        minrightx = (arr1[partx],float('inf')) [partx == x]
        minrighty = (arr2[party],float('inf')) [party == y]

        if maxleftx <= minrighty and minrightx >= maxlefty:
            if x + y % 2 == 0:
                return (max(maxleftx,maxlefty) + min(minrightx,minrighty)) / 2
            else:
                return max(maxleftx,maxlefty)
        elif minrightx < maxlefty:
            low = partx + 1
        else:
            high = partx - 1
        


arr1 = [1,3,8,9,15]
arr2 = [7,11,18,19,21,25]
print median(arr1,arr2)
