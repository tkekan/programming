def removeInvalidParentheses( s):
    """
    :type s: str
    :rtype: List[str]
    """
    result = []
    remove(s, result, 0, 0, ('(', ')'))
    return result
    
def remove( s, result, last_i, last_j, par):
    count = 0
    for i in xrange(last_i, len(s)):
	count += (s[i] == par[0]) - (s[i] == par[1])
	if count >= 0:
	    continue
	for j in xrange(last_j, i + 1):
	    if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
		remove(s[:j] + s[j + 1:], result, i, j, par)
	return
    reversed_s = s[::-1]
    if par[0] == '(':
	remove(reversed_s, result, 0, 0, (')', '('))
    else:
	result.append(reversed_s)

result = removeInvalidParentheses('(((')
print result
