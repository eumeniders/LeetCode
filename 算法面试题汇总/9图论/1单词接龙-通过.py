class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)
        stack=[(beginWord,0)]
        string = 'abcdefghijklmnopqrstuvwxyz'
        while stack:
            word,step = stack.pop(0)
            if word==endWord:
                return step+1
            for i in range(len(word)):
                for j in range(26):
                    tmp = word[:i]+string[j]+word[i+1:]
                    if tmp in wordset:
                        stack.append((tmp,step+1))
                        wordset.remove(tmp)
        return 0
