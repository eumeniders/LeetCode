"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        h=Node(0,None,None)
        h1=h
        h2=h
        p=head
        dic={}
        while p:
            n=Node(p.val,None,p.random)
            h.next=n
            h=h.next
            dic[p]=h
            p=p.next
        while h1.next:
            h1=h1.next
            if h1.random!=None:
                h1.random=dic[h1.random]
        return h2.next
