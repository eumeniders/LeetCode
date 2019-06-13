class Solution(object):
    def itb(self,i):
        b = bin(i)[2:]
        while 8-len(b):
            b='0'+b
        return b
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for x in data:
            a = self.itb(x)
            if count==0:
                if a[0]=='0':
                    continue
                elif a[:3]=='110':
                    count = 1
                elif a[:4]=='1110':
                    count = 2
                elif a[:5]=='11110':
                    count = 3
                else:
                    return False
            else:
                if a[:2]=='10':
                    count-=1
                else:
                    return False
        return count==0
            
                
