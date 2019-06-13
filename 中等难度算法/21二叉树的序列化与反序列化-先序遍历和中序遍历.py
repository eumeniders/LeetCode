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
        def preorder(root):
            if not root:
                return []
            else:
                return [root.val]+preorder(root.left)+preorder(root.right)
        
        def inorder(root):
            if not root:
                return []
            else:
                return inorder(root.left)+[root.val]+inorder(root.right)
        
        pre = preorder(root)
        ino = inorder(root)
        return [pre,ino]
          

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        pre,ino = data[0],data[1]
        def build(pre,ino):
            print pre,ino
            tmp = pre[0]
            index = ino.index(tmp)
            left_ino = ino[:index]
            left_len = len(left_ino)
            right_ino = ino[left_len+1:]
            left_pre = pre[1:left_len+1]
            right_pre = pre[left_len+1:]
            root = TreeNode(tmp)
            if left_pre:
                root.left=build(left_pre,left_ino)
            if right_pre:
                root.right= build(right_pre,right_ino)
            return root
        if pre:
            return build(pre,ino)
        else:
            return []
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
