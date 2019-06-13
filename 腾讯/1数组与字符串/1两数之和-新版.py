class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num = sorted(nums)
        while num:
            tmp = num.pop(0)
            if target-tmp in num:
                if target-tmp!=tmp:
                    return [nums.index(tmp),nums.index(target-tmp)]
                else:
                    idx1 = nums.index(tmp)
                    nums.remove(tmp)
                    idx2 = nums.index(tmp)+1
                    print idx1,idx2
                    return [idx1,idx2]
