def reverseOnlyLetters(S):
    """
    :type S: str
    :rtype: str
    """
    if not S or len(S) == 1:
        return S
    
    left = 0
    right = len(S)-1
    S = list(S)
    while left < right:
        if S[left].isalpha() and S[right].isalpha():
            S[left],S[right] = S[right],S[left]
            left += 1
            right -= 1
        elif S[left].isalpha() and not S[right].isalpha():
            right -= 1
        else:
            left -= 1
    return ''.join(S)

S = "a-bC-dEf-ghIj"
print reverseOnlyLetters(S)
