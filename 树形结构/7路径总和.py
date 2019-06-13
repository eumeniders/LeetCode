# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        t = sum-root.val
        if root.left==None and root.right==None:
            return t==0
        return self.hasPathSum(root.left,t) or self.hasPathSum(root.right,t)
