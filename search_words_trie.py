class DictNode(object):
    def __init__(self):
        self.word = False
        self.children = {}
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = DictNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        if not word:
            return
        mroot = self.root
        for ch in word:
            if ch in mroot.children:
                mroot = mroot.children[ch]
                continue
            else:
                mroot.children[ch] = DictNode()
                mroot = mroot.children[ch]
        mroot.word = True
        
    def util(self, word, mroot):
        for i,ch in enumerate(word):
            if ch == '.':
                tmp = word[i+1:]
                for child in mroot.children:
                    ret = self.util(tmp,mroot.children[child])
                    if ret == True:
                        return True
                return False
            else:
                #print ch,mroot
                if ch not in mroot.children:
                    return False
                mroot = mroot.children[ch]
        return mroot.word
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        mroot = self.root
        return self.util(word,mroot)

w = WordDictionary()
w.addWord("bad")
w.addWord("cat")
w.addWord("baad")
print w.search("b..")
