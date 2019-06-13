# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        res = []
        stack = [root]
        while stack:
            res.append([x.val for x in stack])
            tmp = []
            for i in range(len(stack)):
                if stack[i].left:
                    tmp.append(stack[i].left)
                if stack[i].right:
                    tmp.append(stack[i].right)
            stack = tmp
        return res
