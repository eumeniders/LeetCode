class Solution(object):
    def maxProfit(self, list1):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits = 0
        have_stock = 0
        buy = 0
        for i in range(len(list1)-1):
            if list1[i]<list1[i+1] and have_stock==0:
                buy = list1[i]
                have_stock = 1
                if i == len(list1) - 2:
                    sell = list1[i+1]
                    profits += sell - buy
                    have_stock = 0
            if list1[i]>buy and have_stock ==1:
                if list1[i]>list1[i+1]:
                    sell = list1[i]
                    profits += sell - buy
                    have_stock = 0
                elif i == len(list1) - 2:
                    sell = list1[i+1]
                    profits += sell - buy
                    have_stock = 0
        return profits    
