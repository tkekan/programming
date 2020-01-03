class DictNode(object):
    def __init__(self):
        self.child = {}
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = DictNode()
    
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = DictNode()
            node = node.child[c]
        node.word = True
        return
       



troot = Trie()
troot.addWord("bad")
troot.addWord("dad")
print troot.root.child
