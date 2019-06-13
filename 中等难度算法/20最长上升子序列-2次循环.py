class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins)
        dp=[65535]*(amount+1)
        dp[0]=0
        for j in range(len(coins)):
            for i in range(1,amount+1):
                if i >= coins[j]:
                    dp[i]=min(dp[i-coins[j]]+1,dp[i])
        if dp[amount]==65535:
            return -1
        else:
            return dp[amount]
