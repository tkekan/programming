



d = {0:"", 1:"", 2: "abc", 3: "def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}


def printLetters(num, n, curr, results):
    if curr == n:
        #print ''.join(results)
        results_full.append(''.join(results))
        return

    for i in range(0, len(d[num[curr]])):
        results.append(d[num[curr]][i])
        printLetters(num, n, curr+1, results)
        results.pop()
        
numbers = [2,7]
results = []
results_full = []
printLetters(numbers, len(numbers), 0, results)
print results_full
