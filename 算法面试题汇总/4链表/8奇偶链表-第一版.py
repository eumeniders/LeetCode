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
        if head == None:
            return head
        ou_head = head.next
        ji_zhi = head
        ou_zhi = head.next
        while ji_zhi or ou_zhi:
            if ou_zhi==None or ou_zhi.next==None:
                ji_zhi.next = ou_head
                return head
            ji_zhi.next = ou_zhi.next
            ji_zhi = ji_zhi.next
            ou_zhi.next = ji_zhi.next
            ou_zhi = ou_zhi.next
