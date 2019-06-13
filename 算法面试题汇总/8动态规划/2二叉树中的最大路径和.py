# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max=float('-inf')
    def mx(self,root):
        if not root:
            return 0
        left = self.mx(root.left)
        right = self.mx(root.right)
        tmp = max(root.val,root.val+left,root.val+right)
        self.max = max(tmp,self.max,root.val+left+right)
        return tmp
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.mx(root)
        return self.max
