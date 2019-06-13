class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        stack = ['/']
        tmp = ''
        for i in range(1,len(path)):
            if path[i]!='/' and path[i]!='.':
                tmp+=path[i]
            if path[i]=='.':
                if tmp=='':
                    tmp='.'
                elif tmp=='.':
                    if len(stack)>1:
                        stack.pop()
                    tmp = ''
            if path[i]=='/':
                if tmp=='.':
                    tmp=''
                elif tmp!='':
                    stack.append(tmp+'/')
                    tmp = ''
                else:
                    continue
        stack = ''.join(stack)
        if stack[-1]=='/' and len(stack)>1:
            stack = stack[:-1]
        return stack
