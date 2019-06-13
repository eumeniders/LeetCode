class Solution(object):
    def maxProfit(self, list1):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(list1)<2:
            return 0
        buy = list1[0]
        mx = 0
        for i in range(1,len(list1)):
            buy = min(buy,list1[i])
            if i==len(list1)-1:
                mx +=max(0,list1[i]-buy)
                return mx
            if list1[i]>buy and list1[i]>list1[i+1]:
                mx += list1[i]-buy
                buy = list1[i]
