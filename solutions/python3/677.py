class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.dic = defaultdict(int)

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dic[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sm = 0
        for k in self.dic:
            if k[:len(prefix)] == prefix: sm += self.dic[k]
        return sm


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)