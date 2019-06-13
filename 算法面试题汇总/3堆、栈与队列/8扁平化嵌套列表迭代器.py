# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.idx=0
        self.array=[]
        self.dfs(nestedList)
        
    def dfs(self,nestedList):
        if not nestedList:
            return
        node = nestedList[0]
        if node.isInteger():
            self.array.append(node.getInteger())
            self.dfs(nestedList[1:])
        else:
            self.dfs(node.getList())
            self.dfs(nestedList[1:])
            

    def next(self):
        """
        :rtype: int
        """
        tmp = self.array[self.idx]
        self.idx+=1
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.idx<len(self.array):
            return True
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
