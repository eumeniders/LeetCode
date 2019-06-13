class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        dig='0123456789'
        stack = []
        res = []
        tmp = ''
        for i in range(len(s)):
            if i==len(s)-1:
                if s[i] in dig:
                    tmp+=s[i]
                if tmp:
                    stack.append(int(tmp))
            if s[i]==' ':
                continue
            if s[i] in dig:
                tmp+=s[i]
            else:
                stack.append(int(tmp))
                tmp=''
                stack.append(s[i])
        print stack
        i=0
        while i<len(stack):
            if stack[i] not in ['*','/']:
                res.append(stack[i])
                i+=1
            else:
                tmp=res.pop()
                if stack[i]=='*':
                    tmp*=stack[i+1]
                    i+=2
                    res.append(tmp)
                    continue
                if stack[i]=='/':
                    tmp/=stack[i+1]
                    i+=2
                    res.append(tmp)
                    continue
        a = res[0]
        for i in range(1,len(res)):
            if res[i] not in ['+','-']:
                continue
            if res[i]=='+':
                a+=res[i+1]
            if res[i]=='-':
                a-=res[i+1]
        return a
                
                    
