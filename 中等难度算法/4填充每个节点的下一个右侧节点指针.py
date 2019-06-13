class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        layer = [root]
        while layer:
            tmp = []
            print layer
            for i in range(len(layer)):
                if i != len(layer)-1:
                    layer[i].next=layer[i+1]
                if layer[i].left:
                    tmp.append(layer[i].left)
                    tmp.append(layer[i].right)
            layer=tmp
        return root
