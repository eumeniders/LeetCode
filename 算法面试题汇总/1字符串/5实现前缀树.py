class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie=[]

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        self.trie=[word]+self.trie
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word in self.trie:
            return True
        return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not self.trie:
            return False
        l = len(prefix)
        for x in self.trie:
            if prefix==x[:l]:
                return True
        return False
            
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
