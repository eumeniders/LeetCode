class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.key=[]
        self.val=[]
        self.capacity=capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.key:
            idx = self.key.index(key)
            self.key.pop(idx)
            val = self.val.pop(idx)
            self.key.append(key)
            self.val.append(val)
            return val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key:
            idx = self.key.index(key)
            self.key.pop(idx)
            self.val.pop(idx)
            self.key.append(key)
            self.val.append(value)
        elif self.capacity>0:
            self.key.append(key)
            self.val.append(value)
            self.capacity-=1
        else:
            self.key.pop(0)
            self.val.pop(0)
            self.key.append(key)
            self.val.append(value)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
