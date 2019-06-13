# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root.right)
                root=root.left
            else:
                root = stack.pop()
        return res
