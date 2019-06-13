# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        tmp = []
        for i in range(len(lists)):
            if lists[i]!=None:
                tmp.append(lists[i])
        lists=tmp
        res = ListNode(0)
        head = res
        while lists:
            tmp = [x.val for x in lists]
            idx = tmp.index(min(tmp))
            p = lists[idx].next
            res.next = lists[idx]
            res = res.next
            res.next = None
            lists[idx] = p
            if lists[idx]==None:
                lists.pop(idx)
        return head.next
            
