# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        stack=[]
        res = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root.right)
                root=root.left
            else:
                res.append('#')
                root=stack.pop()
        return res+['#']
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root=None
        a = data.pop(0)
        if a!='#':
            root=TreeNode(a)
            root.left=self.deserialize(data)
            root.right=self.deserialize(data)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
