

class Trie():
    def __init__(self):
        self.child = [None for i in range(0,27)]
        self.isLeaf = False
    
        



root = Trie()
root.child[0] = True
root.child[0] = Trie()
print root.child
