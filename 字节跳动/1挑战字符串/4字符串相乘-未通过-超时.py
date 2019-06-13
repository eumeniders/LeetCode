class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def mul(s1,s2):
            l1 = len(s1)
            l2 = len(s2)
            cin = 0
            if l2>l1:
                s1,s2=s2,s1
                l1,l2=l2,l1
            rs = []
            for i in range(l1-1,-1,-1):
                res = []
                for j in range(l2-1,-1,-1):
                    tmp = long(s2[j])*long(s1[i])+cin
                    cin = tmp/10
                    res = [tmp%10]+res
                    if j==0 and cin!=0:
                        res = [cin]+res
                res+=[0]*(l1-i-1)
                rs.append(long(''.join([str(x) for x in res])))
            return sum([int(x) for x in rs])
        num1 = [long(x) for x in num1]
        num2 = [long(x) for x in num2]
        return mul(num1,num2)
