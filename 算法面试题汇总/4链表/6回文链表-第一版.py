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
        nums = 0
        if head ==None:
            return True
        count = head
        while(count):
            nums += 1
            count = count.next
        if nums ==1:
            return True
        last = None
        this = head
        pres = None 
        right = head

        for i in range(nums/2):
            pnext = this.next
            this.next = last
            last = this
            this = pnext
            right = this
            if i == (nums/2)-1:
                pres = last
        left = pres
        if nums%2 ==1:
            right = right.next
        while(left):
            print left.val,right.val
            if left.val==right.val:
                left = left.next
                right = right.next
                if left ==None:
                    return True
            else:
                return False
            
