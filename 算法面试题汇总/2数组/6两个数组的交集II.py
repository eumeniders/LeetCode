class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        i=0
        res = []
        while i<len(nums1) and nums2:
            if nums1[i] in nums2:
                res.append(nums1[i])
                nums2.remove(nums1[i])
            i+=1
        return res
