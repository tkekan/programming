def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    
    stack_l = [[1,""]]
    res = ""

    for i in range(len(s)):
        if s[i].isdigit():
            res += s[i]
            continue
        elif s[i] == '[':
            stack_l.append([int(res),""])
            res = ""
            continue
        elif s[i] == ']':
            temp_s = stack_l[-1][0] * stack_l[-1][1]
            stack_l.pop()
            stack_l[-1][1] = str(temp_s)
        else:
            stack_l[-1][1] += s[i]
    ret = stack_l[-1][1]
    return ret

print decodeString("3[a]2[bc]")
