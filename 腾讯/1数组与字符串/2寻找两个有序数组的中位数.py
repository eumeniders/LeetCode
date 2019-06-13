class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1+nums2
        num.sort()
        l = len(num)
        if l%2==0:
            return ((num[l/2-1]+num[l/2])/2.0)
        else:
            return num[l/2]
