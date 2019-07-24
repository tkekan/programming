

def intersect(A , B):
    result = []
    indexA = 0
    indexB = 0
    while indexA < len(A) and indexB < len(B):
        left = max(A[indexA][0], B[indexB][0])
        right = min(A[indexA][1], B[indexB][1])
        if left <= right:
            result.append([left,right])
        if A[indexA][1] < B[indexB][1]:
            indexA += 1
        else: indexB += 1
    print result


a = [[0,2],[5,10],[13,23],[24,25]] 
b = [[1,5],[8,12],[15,24],[25,26]]
intersect(a,b)

