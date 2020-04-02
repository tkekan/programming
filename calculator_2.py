


def evaluate(s):
    op = '+'
    num = 0
    stack = []
    sign = 1
    ss = [1]
    for i,c in enumerate(s):
        if c == ' ':
            continue
        if s[i].isdigit():
            num = num * 10 + ord(s[i]) - ord('0')
        if not s[i].isdigit() or i == len(s) - 1:
            if s[i] == '(':
                ss.append(sign * ss[-1])
                sign = 1
                continue
            elif s[i] == ')':
                stack.append(num * sign * ss[-1])
                ss.pop()
                sign = 1
                continue
            elif op == '+':
                stack.append(num * sign * ss[-1])
                sign = 1
            elif op == '-':
                stack.append(num * sign * ss[-1])
                sign = -1
            elif op == '*':
                tmp = stack.pop()
                stack.append(tmp * num * sign * ss[-1])
            elif op == '/':
                tmp =stack.pop()
                stack.append(tmp / num * sign * ss[-1])
            num = 0
            op = c
    return sum(stack)






s = "(4 + 3)/2"
print evaluate(s)

