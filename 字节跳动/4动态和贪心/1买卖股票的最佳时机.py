class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        buy = prices[0]
        mx = 0
        for i in range(1,len(prices)):
            buy = min(buy,prices[i])
            mx = max(prices[i]-buy,mx)
        return mx
