class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num=[]
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.num.append(num)
        self.num.sort()
        

    def findMedian(self):
        """
        :rtype: float
        """
        n=len(self.num)
        if n%2==0:
            return float(self.num[n/2-1]+self.num[n/2])/2
        return float(self.num[n/2])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
