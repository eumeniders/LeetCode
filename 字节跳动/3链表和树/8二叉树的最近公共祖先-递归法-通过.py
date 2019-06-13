# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bl(self,root):
        res = []
        stack = [root]
        while stack:
            tmp = stack.pop()
            if tmp==None:
                continue
            res.append(tmp.val)
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
        return res
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        res = root
        if (p.val in self.bl(root.left)) and (q.val in self.bl(root.left)):
            return self.lowestCommonAncestor(root.left,p,q)
        elif (p.val in self.bl(root.right)) and (q.val in self.bl(root.right)):
            return self.lowestCommonAncestor(root.right,p,q)
        return res
                
                
