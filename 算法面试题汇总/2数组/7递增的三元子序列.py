class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """ 
        if len(nums)<3:
            return False
        a,b = 2**32,2**32
        for i in range(len(nums)):
            if nums[i]<=a:
                a = nums[i]
            elif nums[i]<=b:
                b = nums[i]
            else:
                return True
        return False
        
