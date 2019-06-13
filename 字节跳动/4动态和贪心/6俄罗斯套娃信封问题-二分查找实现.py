import bisect
class Solution:
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        res, n = 0, len(envelopes)
        envelopes.sort(key=lambda a:(a[0], -a[1]))
        mem = []
        for e in envelopes:
            index = bisect.bisect_left(mem, e[1])
            if len(mem) == index:
                mem.append(e[1])
            else:
                mem[index] = e[1]
        return len(mem)
b = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
a=Solution()
print a.maxEnvelopes(b)
