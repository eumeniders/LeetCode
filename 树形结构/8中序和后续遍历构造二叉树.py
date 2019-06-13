# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        root = ListNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        ll = len(inorder[:idx])
        root.left=self.buildTree(inorder[:idx],postorder[:ll])
        root.right=self.buildTree(inorder[idx+1:],postorder[ll:-1])
        return root
