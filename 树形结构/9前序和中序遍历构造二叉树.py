# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder==[]:
            return None
        root =ListNode(preorder[0])
        idx = inorder.index(preorder[0])
        ll = len(inorder[:idx])
        root.left=self.buildTree(preorder[1:1+ll],inorder[:idx])
        root.right=self.buildTree(preorder[1+ll:],inorder[idx+1:])
        return root
    
            
