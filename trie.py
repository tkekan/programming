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
        node.isWord = True
        return
    
    def search(self, word):
        root = self.root
        for c in word:
            if c in root.child:
                root = root.child[c]
            else:
                return False
        return root.isWord
       



troot = Trie()
troot.addWord("bad")
troot.addWord("dad")
troot.addWord("badal")
print troot.search("badass")
print troot.search("badal")
print troot.search("bad")
print troot.root.child
