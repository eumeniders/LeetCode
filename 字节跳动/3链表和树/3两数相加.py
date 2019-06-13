# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cin = 0
        l3 = ListNode(0)
        head = l3
        while l1 or l2:
            tmp = 0
            if l1:
                tmp+=l1.val
                l1=l1.next
            if l2:
                tmp+=l2.val
                l2=l2.next
            tmp+=cin
            l3.next=ListNode(tmp%10)
            l3= l3.next
            cin = tmp/10
        if cin>0:
            l3.next=ListNode(cin)
        return head.next
