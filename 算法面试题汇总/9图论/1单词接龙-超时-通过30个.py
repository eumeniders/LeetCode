class Solution(object):
    def isval(self,a,b):
        num = 0
        la = len(a)
        for i in range(la):
            if a[i]!=b[i]:
                num+=1
            if num==2:
                return False
        if num==1:
            return True
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        stack=[(beginWord,0)]
        while stack:
            word,step = stack.pop(0)
            if word==endWord:
                return step+1
            l,r=0,len(wordList)
            while l<r:
                if self.isval(word,wordList[l]):
                    stack.append((wordList[l],step+1))
                    wordList.remove(wordList[l])
                    r-=1
                else:
                    l+=1
        return 0
