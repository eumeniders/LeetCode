class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list1 = []
        for i in range(len(nums)):
            if target >= 0:
                if nums[i]<=target and target-nums[i] in nums:
                    b = nums.index(target-nums[i])
                    if i == b:
                        continue
                    else:
                        list1.append(i)
                        list1.append(b)
                        return list1
            else:
                if nums[i]>=target and target-nums[i] in nums:
                    b = nums.index(target-nums[i])
                    if i == b:
                        continue
                    else:
                        list1.append(i)
                        list1.append(b)
                        return list1
