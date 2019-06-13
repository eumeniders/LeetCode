class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = ''
        max_ = 0
        for i in xrange(len(s)):
            if s[i] not in tmp:
                tmp+=s[i]
            else:
                max_ = max(max_,len(tmp))
                idx = tmp.index(s[i])
                tmp = tmp[idx+1:]+s[i]
            if i==len(s)-1:
                max_=max(max_,len(tmp))
        return max_
