class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def build(self, preorder, inorder):
        #print preorder
        root_val = preorder[0]
        left_inorder = inorder[:inorder.index(root_val)]
        left_len = len(left_inorder)
        right_inorder = inorder[inorder.index(root_val)+1:]
        left_preorder = preorder[1:1+left_len]
        right_preorder = preorder[1+left_len:]
        root = TreeNode(preorder[0])
        if left_preorder:
            root.left = self.build(left_preorder,left_inorder)
        if right_preorder:
            root.right = self.build(right_preorder,right_inorder)
        return root
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder==[]:
            return None
        root = self.build(preorder, inorder)   
        return root
    
