class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums=map(str,nums)
        nums.sort(cmp=lambda x,y:1 if x+y>y+x else -1 if x+y<y+x else 0,reverse=True)
        res = ''.join(nums)
        if res[0]=='0':
            return '0'
        return res
