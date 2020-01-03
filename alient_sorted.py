def isAlienSorted(words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        
        d = {}
        for i,c in enumerate(order):
            d[c] = i
        
        for i in range(0, len(words)-1):
            j = i+1
            x = words[i]
            y = words[j]
            for k in range(min(len(x),len(y))):
                if x[k] !=y[k]:
                    if d[x[k]] > d[y[k]]:
                        return False
                    break
            else:
               if len(x) > len(y):
                  return False
        return True


words = ["kuvp","q"]
words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
#order = "ngxlkthsjuoqcpavbfdermiywz"
print isAlienSorted(words, order)
