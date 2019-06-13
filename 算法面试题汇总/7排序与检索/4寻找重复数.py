class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow=fast=0
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        fast=0
        while 1:
            slow = nums[slow]
            fast = nums[fast]
            if slow==fast:
                break
        return slow
