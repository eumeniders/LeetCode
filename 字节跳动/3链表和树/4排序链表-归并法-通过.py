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
        if head==None or head.next==None:
            return head
        s,f=head,head
        while s:
            if s.next:
                s=s.next
            else:
                break
            if s.next:
                s=s.next
                f=f.next
            else:
                break
        p = f.next
        f.next = None
        f = head
        p1 = self.sortList(f)
        p2 = self.sortList(p)
        return self.merge(p1,p2)
    def merge(self,left,right):
        if left==None:
            return right
        if right==None:
            return left
        if left.val<=right.val:
            left.next=self.merge(left.next,right)
            return left
        else:
            right.next=self.merge(left,right.next)
            return right
