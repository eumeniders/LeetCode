class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==[0]:
            return True
        i=0
        while i < len(nums):
            max=0
            tmp = 0
            for j in range(1,nums[i]+1):
                if i+j>=len(nums)-1:
                    return True
                if j+nums[i+j]>max:
                    max = j+nums[i+j]
                    tmp = j
            if max==0:
                return False
            i+=tmp
            if i>=len(nums)-1:
                return True
        return False
