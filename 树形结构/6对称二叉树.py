# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.isequal(root.left,root.right)
    def isequal(self,left,right):
        if left==None and right==None:
            return True
        if (left==None and right!=None) or (left!=None and right==None):
            return False
        if left.val==right.val:
            return self.isequal(left.right,right.left) and self.isequal(left.left,right.right)
            
            
            
            
            
