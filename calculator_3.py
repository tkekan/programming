

def evaluate(s):
    stack = [1]
    sign = 1
    num = 0
    ans = 0
    for i,c in enumerate(s):
        if c == ' ':
            continue
        elif 0 <= (ord(c) - ord('0')) <= 9:
            num = num * 10 + (ord(c) - ord('0'))
            #print num
        elif c == '+' or c == '-':
            ans = ans + num * sign * stack[-1]
            sign = (1,-1) [ c == '-']
            num = 0
        elif c == '(':
            stack.append(sign * stack[-1])
            sign = 1
        elif c == ')':
            ans = ans + num * sign * stack[-1]
            stack.pop()
            sign = 1
            num = 0
    if num:
        ans = ans + num * sign * stack[-1]
    return ans


s = "(5-(1+(5)))"
print evaluate(s)
