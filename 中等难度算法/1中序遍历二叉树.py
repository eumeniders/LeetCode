#coding=utf-8
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):#递归方法1
    def __init__(self):
        self.list = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.inorderTraversal(root.left)
            self.list.append(root.val)
            self.inorderTraversal(root.right)
        return self.list

class Solution1(object):#递归方法2
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
        else:
            return []
    
class Solution2(object):#非递归方法
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while root or stack:
            if root:
                stack.append(root)
                root=root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root=root.right
        return res 


a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
a.left=b
a.right=c
b.left=d
c.right=e

s = Solution()
s1= Solution1()
print s1.inorderTraversal(a)
