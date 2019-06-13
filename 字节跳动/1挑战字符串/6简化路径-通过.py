class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        x = path.split('/')
        for i in x:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if res:
                    res.pop()
            else:
                res.append(i)
        return '/'+'/'.join(res)  
