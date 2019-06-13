class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        if l==0:
            return -1
        if target>nums[0]:
            for i in xrange(l):
                if target==nums[i]:
                    return i
        else:
            for i in xrange(l-1,-1,-1):
                if target==nums[i]:
                    return i
        return -1
