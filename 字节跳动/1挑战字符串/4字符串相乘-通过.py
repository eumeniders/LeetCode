class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=='0' or num2=='0':
            return '0'
        l1 = len(num1)
        l2 = len(num2)
        k = [0]*(l1+l2)
        for i in range(l1-1,-1,-1):
            for j in range(l2-1,-1,-1):
                k[i+j+1]+=int(num1[i])*int(num2[j])
        cin = 0
        for i in range(l1+l2-1,-1,-1):
            k[i] += cin 
            cin = k[i]/10
            k[i] = k[i]%10
        for i in range(l1+l2):
            if k[i]!=0:
                return ''.join([str(x) for x in k[i:]])
