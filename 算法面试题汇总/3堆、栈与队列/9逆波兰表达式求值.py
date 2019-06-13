class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ys = ['+','-','*','/']
        stack = []
        for x in tokens:
            if x in ys:
                b = stack.pop()
                a = stack.pop()
                if x=='+':
                    stack.append(int(a)+int(b))
                elif x=='-':
                    stack.append(int(a)-int(b))
                elif x=='*':
                    stack.append(int(a)*int(b))
                elif x=='/':
                    stack.append(int(float(a)/float(b)))
            else:
                stack.append(x)
        return stack[0]
