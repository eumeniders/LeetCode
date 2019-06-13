# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res=ListNode(-2**32)
        p = head
        while p:
            n = res
            while n:
                if p.val>n.val:
                    if n.next and p.val>n.next.val:
                        n=n.next
                    else:
                        tmp = n.next 
                        n.next=ListNode(p.val)
                        n = n.next
                        n.next = tmp
                        break
            p =p.next
        return res.next
