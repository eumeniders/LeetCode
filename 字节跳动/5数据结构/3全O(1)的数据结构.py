class Node:
    """
    定义双向链表的节点 双向链表用于按顺序存储(key,value)
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numDict = dict()  # 用于存储key与双向链表中node(key,node)映射关系
        self.head = Node("", -1)  # 头节点 存储最小值
        self.tail = Node("", -1)  # 尾节点 存储最大值
        # 初始化双向链表
        self.tail.prev = self.head
        self.head.next = self.tail

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        # 新增key,插入到numDict中,并放置在双向链表head->next
        if key not in self.numDict:
            insNode = Node(key, 1)  # 初始化新增节点
            self.numDict[key] = insNode  # 将这个节点放置到我们的字典当中
            insNode.next = self.head.next  # 第一步：进行双向链表拼接  这一步是断开head和下一个节点的连接
            self.head.next.prev = insNode  # 拼接第二步
            self.head.next = insNode  # 第三步
            insNode.prev = self.head  # 第四步
        else:
            # 存量key
            curNode = self.numDict[key]
            curNode.value += 1
            # 通过交换节点的方式保持双向链表有序
            while curNode.next != self.tail and curNode.value > curNode.next.value:
                prevNode = curNode.prev  # 保存前一个节点
                nextnextNode = curNode.next.next  # 保存curNode的next节点的next
                prevNode.next = curNode.next
                prevNode.next.prev = prevNode
                prevNode.next.next = curNode
                curNode.prev = prevNode.next
                curNode.next = nextnextNode
                nextnextNode.prev = curNode

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.numDict:
            return
        curNode = self.numDict[key]
        if curNode.value == 1:
            # 在双向链表中删除该节点
            prevNode = curNode.prev
            nextNode = curNode.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
        else:
            # 该key对应的value减1 并通过交换节点的方式保持双向链表有序
            curNode.value -= 1
            while curNode.prev != self.head and curNode.value < curNode.prev.value:
                prepreNode = curNode.prev.prev
                nextNode = curNode.next
                nextNode.prev = curNode.prev
                curNode.prev.prev = curNode
                curNode.prev = prepreNode
                curNode.next = nextNode.prev
                nextNode.prev.next = nextNode
                prepreNode.next = curNode

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return self.tail.prev.key if self.tail.prev != self.head else ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return self.head.next.key if self.head.next != self.tail else ""
