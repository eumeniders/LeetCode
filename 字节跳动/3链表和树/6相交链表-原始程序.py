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
        if headA==None or headB==None:
            return None
        a,b = headA,headB
        lena=lenb=1
        while a.next:
            lena+=1
            a=a.next
        while b.next:
            lenb+=1
            b=b.next
        m,n = headA,headB
        if lena>=lenb:
            for i in range(lena-lenb):
                m=m.next
        else:
            for i in range(lenb-lena):
                n=n.next
        while m!=n:
            m=m.next
            n=n.next
        return m
            

        
