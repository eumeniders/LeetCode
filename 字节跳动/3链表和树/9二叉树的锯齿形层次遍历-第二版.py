# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        layer = [root]
        layer_list = []
        while layer:
            layer_list.append([x.val for x in layer])
            tmp = []
            for x in layer:
                if x==None:
                    continue
                if x.left:
                    tmp.append(x.left)
                if x.right:
                    tmp.append(x.right)
            layer = tmp
        for i in range(len(layer_list)):
            if i%2==1:
                layer_list[i].reverse()
        return layer_list
                
            
        
