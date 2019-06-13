# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        p,q=head,head
        count=1
        l=None
        while q:
            if q.next:
                q=q.next
                count+=1
            else:
                break
            if q.next:
                count+=1
                q=q.next
                r=p.next
                p.next=l
                l=p
                p=r
            else:
                break
        q=p.next
        p.next=l
        if count%2==1:
            p=p.next
        while p and q:
            if p.val==q.val:
                p=p.next
                q=q.next
            else:
                return False
        return True
            
