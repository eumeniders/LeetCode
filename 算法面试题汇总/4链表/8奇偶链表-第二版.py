# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        ji,ou=head,head.next
        h=ou
        while ou:
            if ou.next!=None:
                ji.next=ou.next
                ji=ji.next
                ou.next=ji.next
                ou=ou.next
            else:
                break
        ji.next=h
        return head
        
