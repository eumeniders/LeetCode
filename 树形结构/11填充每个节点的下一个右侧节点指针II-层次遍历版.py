"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        stack=[root]
        while stack:
            tmp=[]
            for i in range(len(stack)):
                if stack[i].left:
                    tmp.append(stack[i].left)
                if stack[i].right:
                    tmp.append(stack[i].right)
                if i!=len(stack)-1:
                    stack[i].next=stack[i+1]
            stack = tmp
        return root
