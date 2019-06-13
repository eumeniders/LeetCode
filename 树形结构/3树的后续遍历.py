# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root.left)
                root=root.right
            else:
                root= stack.pop()
        return res[::-1]
            
