class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        tmp = ''
        for i in xrange(len(strs[0])):
            tmp+=strs[0][i]
            for j in xrange(1,len(strs)):
                if tmp!=strs[j][:i+1]:
                    return tmp[:i]
                else:
                    continue
        return tmp
