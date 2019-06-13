# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p,q=headA,headB
        l1=l2=0
        while p:
            l1+=1
            p=p.next
        while q:
            l2+=1
            q=q.next
        if l1>=l2:
            p,q=headA,headB
            l = l1-l2
        else:
            p,q=headB,headA
            l = l2-l1
        while l:
            p = p.next
            l-=1
        while p:
            if p==q:
                return p
            else:
                p=p.next
                q=q.next
        return None
            

        
