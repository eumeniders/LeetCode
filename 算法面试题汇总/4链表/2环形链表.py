# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p,q=head,head
        while p and q:
            if q.next:
                q=q.next
            else:
                return False
            if q.next:
                q=q.next
                p=p.next
            else:
                return False
            if p==q:
                return True
        return False
