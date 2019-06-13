class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        coins.sort()
        stack = [(amount,0)]
        visited=[0 for _ in range(amount+1)]
        visited[amount]=1
        while stack:
            num,step=stack.pop(0)
            i=0
            tnum=num-coins[i]
            while tnum>=0:
                if tnum==0:
                    return step+1
                if not visited[tnum]:
                    stack.append((tnum,step+1))
                    visited[tnum]=1
                i+=1
                if i==len(coins):
                    tnum=-1
                    break
                tnum=num-coins[i]
        return -1
