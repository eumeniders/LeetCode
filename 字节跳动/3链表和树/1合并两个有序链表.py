class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode(None)
        head = l
        while l1 or l2:
            if not l1:
                l.next=l2
                return head.next
            if not l2:
                l.next=l1
                return head.next
            if l1.val<=l2.val:
                l.next = l1
                l=l.next
                l1=l1.next
            else:
                l.next=l2
                l=l.next
                l2=l2.next

def create(li):
    head = ListNode(li[0])
    a = head
    for i in range(1,len(li)):
        a.next = ListNode(li[i])
        a = a.next
    return head
l1=create([1,2,4])
l2=create([1,3,4])
a=Solution()
print a.mergeTwoLists(l1,l2)
