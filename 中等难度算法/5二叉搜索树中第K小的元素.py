# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        val_list = []
        lst = [root]
        while lst:
            a = lst.pop()
            val_list.append(a.val)
            if a.left:
                lst.append(a.left)
            if a.right:
                lst.append(a.right)
        return sorted(val_list)[k-1]