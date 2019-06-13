class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i,n=0,0
        while i<len(nums) and n<len(nums):
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                n+=1
            else:
                i+=1
        return nums
