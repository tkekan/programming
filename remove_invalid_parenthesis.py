

def isvalid(string):
    cnt = 0
    for index in range(len(string)):
        if string[index] == '(':
            cnt+= 1
        elif string[index] == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0

def removeinvalid(s):
        d = dict()
        q = []
        q.append(s)
        level = False
        results = []
        while len(q):
            string = q.pop(0)
            print string
            if isvalid(string):
                results.append(string)
                level = True
                #If you continue here and remove the level above, you will process all the levels
                # Hence it will give you valid string for all the levels. 
                # But since you are interested only with minimum number of parenthesis to remove, you 
                # once find it, only print the strings of the same level, since you have removed the minimum # of parenthesis. 
                #continue

            if level:
                continue

            for ptr in range(len(string)):
                if string[ptr].isalpha():
                    continue
                temp = string[0:ptr] + string[ptr+1:]
                if d.get(temp, 0) == 0:
                    d[temp] = 1
                    q.append(temp)
        return results

s = "()((()"
s = "()))((()"
s = "()())()"
s = "(k()"
s = "(((k()(("
results = []
print removeinvalid(s)
