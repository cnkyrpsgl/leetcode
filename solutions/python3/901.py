class StockSpanner:

    def __init__(self):
        self.arr = []  
        self.res = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if self.arr and self.arr[-1] > price: self.res.append(1)
        else:
            i = len(self.arr) - 1
            while i >= 0:
                if self.arr[i] <= price and self.res[i]:
                    i -= self.res[i]
                else: break
            self.res.append(len(self.arr) - i)
        self.arr.append(price)
        return self.res[-1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)