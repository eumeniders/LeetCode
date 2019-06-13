#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        layer_list=[]
        layer = [root]
        res = []
        while layer:
            layer_list.append(layer)
            tmp = []
            for i in range(len(layer)):
                if layer[i].left:
                    tmp.append(layer[i].left)
                if layer[i].right:
                    tmp.append(layer[i].right)
            layer=tmp
        for i in range(len(layer_list)):
            tmp = []
            if i%2==0:
                for j in range(len(layer_list[i])):
                    tmp.append(layer_list[i][j].val)
                res.append(tmp)
            else:
                for j in range(len(layer_list[i])):
                    tmp.append(layer_list[i][j].val)
                res.append(tmp[::-1])
        return res
