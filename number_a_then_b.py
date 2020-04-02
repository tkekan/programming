


def number(s):
    rhs = lhs = 0
    for i in range(len(s)):
        if s[i] == 'A':
            rhs += 1

    ans = rhs
    for i in range(len(s)):
        if s[i] == 'A':
            rhs -= 1
        else:
            lhs += 1
        ans = min(ans, rhs+lhs)

    print ans


number("BAABAB")
